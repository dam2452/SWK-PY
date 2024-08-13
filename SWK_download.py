import os
import requests
from tqdm import tqdm
import argparse


def remove_partial_files(directory):
    """Remove all .part files in the specified directory and its subdirectories."""
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.part'):
                file_path = os.path.join(root, file)
                os.remove(file_path)


def get_existing_files_info(base_directory):
    """Get total size of existing fully downloaded files."""
    total_downloaded_size = 0
    total_downloaded_episodes = 0

    for root, dirs, files in os.walk(base_directory):
        for file in files:
            if file.endswith('.mp4'):
                file_path = os.path.join(root, file)
                total_downloaded_size += os.path.getsize(file_path)
                total_downloaded_episodes += 1

    return total_downloaded_size, total_downloaded_episodes


def download_file(url, file_path, overall_bar, episode_bar):
    """Download the file with resume support and a progress bar."""
    temp_file_path = file_path + ".part"
    file_size = 0

    if os.path.exists(temp_file_path):
        file_size = os.path.getsize(temp_file_path)

    headers = {"Range": f"bytes={file_size}-"} if file_size else None

    try:
        with requests.get(url, stream=True, headers=headers) as r:
            r.raise_for_status()
            total_length = int(r.headers.get('content-length', 0)) + file_size
            with tqdm(desc=f"Downloading {os.path.basename(file_path)}", total=total_length, initial=file_size,
                      unit='iB', unit_scale=True, unit_divisor=1024, leave=False) as file_bar:
                with open(temp_file_path, 'ab') as f:
                    for chunk in r.iter_content(chunk_size=1024):
                        if chunk:
                            size = f.write(chunk)
                            file_bar.update(size)
                            overall_bar.update(size)
            episode_bar.update(1)
        os.rename(temp_file_path, file_path)  # Rename temp file to final file name after download completes
    except Exception as e:
        print(f"Failed to download {url}. Error: {e}")
        if os.path.exists(temp_file_path):
            os.remove(temp_file_path)  # Remove incomplete file


def format_episode_name(name, season=None, episode=None, global_episode=None, mode="global"):
    """Formatuje nazwę odcinka zgodnie z ustalonym standardem."""
    name = name.split('. ', 1)[-1] if '. ' in name else name
    safe_name = "".join(c if c.isalnum() else '_' for c in name).replace('_', ' ')
    safe_name = safe_name.replace(' ', '.')
    safe_name = '.'.join(filter(None, safe_name.split('.')))  # Usuwa ciągi kropek

    if mode == "season":
        formatted_name = f"ŚwiatWedługKiepskich.S{int(season):02}E{int(episode):02}.{safe_name}.mp4"
    elif mode == "global":
        formatted_name = f"ŚwiatWedługKiepskich.E{int(global_episode):03}.{safe_name}.mp4"

    return formatted_name


def count_downloaded_episodes(base_directory, season_number, mode):
    """Zlicza liczbę pobranych odcinków w folderze."""
    season_folder = os.path.join(base_directory, f"Season_{season_number}")
    if not os.path.exists(season_folder):
        return 0

    episode_files = [f for f in os.listdir(season_folder) if f.endswith(".mp4")]

    if mode == "season":
        return len(episode_files)
    elif mode == "global":
        # For global mode, consider the largest global episode number found
        max_global_episode = 0
        for file_name in episode_files:
            try:
                global_episode_number = int(file_name.split('.')[1].lstrip("E"))
                max_global_episode = max(max_global_episode, global_episode_number)
            except (IndexError, ValueError):
                continue
        return max_global_episode


def main():
    default_input = os.path.join(os.path.dirname(__file__), "kiepscy.txt")
    default_output = os.path.join(os.path.dirname(__file__), "SWK_downloaded")

    parser = argparse.ArgumentParser(description="Download episodes of 'Świat Według Kiepskich' with resume support.")
    parser.add_argument('--input', type=str, default=default_input,
                        help='Path to the input file (default: kiepscy.txt in the script directory)')
    parser.add_argument('--output', type=str, default=default_output,
                        help='Base output directory (default: SWK_downloaded in the script directory)')
    parser.add_argument('--mode', type=str, choices=['season', 'global'], default='global',
                        help='Numbering mode: "season" or "global" (default: global)')
    parser.add_argument('--episode', type=int, help='Download only the specified global episode number')
    parser.add_argument('--season', type=int, help='Download all episodes from the specified season')

    args = parser.parse_args()

    # Remove all .part files before starting the download process
    remove_partial_files(args.output)

    season_number = '01'
    episode_number = 1
    global_episode_number = 1
    episode_name = "Unknown"

    # Count total episodes and calculate total size
    total_episodes = 0
    total_size = 0
    download_urls = []

    with open(args.input, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            if line.startswith("http"):
                total_episodes += 1
                download_urls.append(line)
                r = requests.head(line, allow_redirects=True)
                total_size += int(r.headers.get('content-length', 0))

    # Get the size and count of already downloaded files
    downloaded_size, downloaded_episodes = get_existing_files_info(args.output)

    # Progress bars
    with tqdm(desc="Total Progress", total=total_size, initial=downloaded_size, unit='iB', unit_scale=True,
              unit_divisor=1024, leave=True) as overall_bar:
        with tqdm(desc="Episode Progress", total=total_episodes, initial=downloaded_episodes, unit='episode',
                  leave=True) as episode_bar:
            with open(args.input, 'r', encoding='utf-8') as file:
                for line in file:
                    line = line.strip()
                    if line.startswith("SEZON"):
                        season_number = line.split()[1].zfill(2)
                        episode_number = 1
                        continue

                    if line and not line.startswith("http"):
                        episode_name = line  # Assume any non-empty line before a URL is the episode name
                        continue

                    if line.startswith("http"):
                        episode_url = line  # Assign episode URL

                        if args.episode and global_episode_number != args.episode:
                            global_episode_number += 1
                            continue

                        if args.season and int(season_number) != args.season:
                            global_episode_number += 1
                            episode_number += 1
                            continue

                        file_name = format_episode_name(episode_name, season=season_number, episode=episode_number,
                                                        global_episode=global_episode_number, mode=args.mode)
                        season_folder = os.path.join(args.output, f"Season_{season_number}")
                        os.makedirs(season_folder, exist_ok=True)
                        file_path = os.path.join(season_folder, file_name)

                        # Check if the file is already fully downloaded
                        if os.path.exists(file_path) and os.path.getsize(file_path) == int(
                                requests.head(episode_url, allow_redirects=True).headers.get('content-length', 0)):
                            print(f"File {file_path} already exists and is fully downloaded, skipping.")
                            episode_bar.update(1)
                            global_episode_number += 1
                            episode_number += 1
                            continue

                        download_file(episode_url, file_path, overall_bar, episode_bar)

                        global_episode_number += 1
                        episode_number += 1

                        if args.episode:
                            break  # Exit after downloading the specified episode

    if args.episode and global_episode_number != args.episode + 1:
        print(f"Episode {args.episode} not found in the input file.")
    elif args.season and int(season_number) != args.season:
        print(f"Season {args.season} not found in the input file.")


if __name__ == '__main__':
    main()
