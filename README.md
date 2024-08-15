# SWK Download Script

This Python script allows you to download episodes of "Świat Według Kiepskich" with resume support. It handles downloading episodes by season or globally numbered episodes, and includes features like partial download removal and progress tracking.

## Important Notice

**Disclaimer:** I am not the author or creator of the `.txt` file, its contents, or any of the links within it. I have no affiliation with the owners or creators of "Świat Według Kiepskich" or any related content. "Świat Według Kiepskich" is the property of Polsat and all rights to the show belong to them. I take no responsibility for the content of the `.txt` file or how it is used. This script is purely a tool written in Python to assist with downloading the episodes listed in the provided `.txt` file.

## Easy Setup Guide

If you're not familiar with programming or installing software, follow these steps to get everything set up. This guide will help you install the necessary tools and run the script easily.

### Step 1: Install Git

Git is a version control system that will help you download the script from GitHub.

1. Open the **Command Prompt** (`cmd`). You can do this by typing `cmd` in the Start Menu and pressing Enter.
2. Type the following command and press Enter:

   ```bash
   winget install --id Git.Git -e --source winget
   ```

3. Wait for the installation to complete.

### Step 2: Install Python

Python is the programming language used to run this script.

1. In the same Command Prompt window, type the following command and press Enter:

   ```bash
   winget install --id Python.Python.3 -e --source winget
   ```

2. Wait for the installation to complete.

### Step 3: Download the Script

1. After installing Git, type the following command to download the script from GitHub:

   ```bash
   git clone https://github.com/yourusername/SWK_download.git
   ```

2. Navigate to the script's directory:

   ```bash
   cd SWK_download
   ```

### Step 4: Install Required Python Libraries

1. Before running the script, you need to install a couple of Python libraries. In the same Command Prompt window, type:

   ```bash
   pip install requests tqdm
   ```

2. Wait for the installation to complete.

### Step 5: Run the Script

Now you're ready to download the episodes!

- **To download all episodes using the default settings**, simply type:

  ```bash
  python SWK_download_resume.py
  ```

- **To download a specific episode (e.g., episode 166)**, type:

  ```bash
  python SWK_download_resume.py --episode 166
  ```

- **To download all episodes from a specific season (e.g., season 3)**, type:

  ```bash
  python SWK_download_resume.py --season 3
  ```

The episodes will be downloaded to a folder called `SWK_downloaded` in the same directory where the script is located.

## Features

- **Resume Support**: Automatically resumes downloads from where they left off.
- **Progress Bars**: Provides real-time progress bars for both individual episodes and total download progress.
- **Partial File Cleanup**: Removes incomplete files before starting a new download session.
- **Flexible Numbering Modes**: Supports both season-based and global episode numbering.
- **Selective Downloading**: Allows downloading a specific episode or all episodes from a particular season.

## Requirements

- Python 3.6 or higher
- `requests` library
- `tqdm` library

These requirements are automatically installed if you follow the Easy Setup Guide above.

## Usage

### Default Usage

If you want to use the default input (`kiepscy.txt` in the script's directory) and output (`SWK_downloaded` in the script's directory), simply run:

```bash
python SWK_download_resume.py
```

### Custom Usage

You can customize the input file and output directory paths using the `--input` and `--output` options:

```bash
python SWK_download_resume.py --input /path/to/your/kiepscy.txt --output /path/to/output/directory
```

### Downloading Specific Episode

To download a specific episode by its global number:

```bash
python SWK_download_resume.py --episode 166
```

### Downloading a Full Season

To download all episodes from a specific season:

```bash
python SWK_download_resume.py --season 3
```

## Input File Format

The input file (`kiepscy.txt`) should list the seasons and episode URLs in the following format:

```plaintext
SEZON 1
http://example.com/episode1.mp4
Episode Name 1
http://example.com/episode2.mp4
Episode Name 2

SEZON 2
http://example.com/episode3.mp4
Episode Name 3
```

## Example

Here's an example of running the script to download all episodes from season 3:

```bash
python SWK_download_resume.py --season 3
```

## Contribution

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/yourusername/SWK_download/issues).

## License

This project is licensed under an open license, allowing anyone to use, modify, and distribute the code without restriction.
```

### Jak używać:

1. **Skopiuj** powyższą treść do pliku `README.md`.
2. **Zastąp** `yourusername` swoim użytkownikiem GitHub w linkach do repozytorium, jeśli chcesz umożliwić zgłaszanie problemów i próśb o nowe funkcje.
3. **Dodaj** plik do swojego repozytorium GitHub.

Ten README zapewnia pełne informacje dla użytkowników, zarówno tych zaawansowanych, jak i początkujących, oraz zawiera wszystkie istotne zastrzeżenia dotyczące praw autorskich i odpowiedzialności.