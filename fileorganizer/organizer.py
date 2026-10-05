from pathlib import Path
import shutil


def validate_directory(directory):
    path = Path(directory)

    if not path.exists():
        print(f"Error: directory does not exist: {directory}")
        return False

    if not path.is_dir():
        print(f"Error: not a directory: {directory}")
        return False

    return True


FILE_CATEGORIES = {
    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".gif": "Images",

    ".pdf": "Documents",
    ".doc": "Documents",
    ".docx": "Documents",
    ".txt": "Documents",

    ".mp3": "Music",
    ".wav": "Music",
    ".flac": "Music",

    ".mp4": "Videos",
    ".mkv": "Videos",
    ".avi": "Videos",
}


def get_category(file):
    suffix = file.suffix.lower()

    return FILE_CATEGORIES.get(suffix, "Others")

def create_category_dirs(directory):
    path = Path(directory)

    categories = set(FILE_CATEGORIES.values())
    categories.add("Others")

    for category in categories:
        (path / category).mkdir(exist_ok=True)

def get_unique_destination(destination):
    if not destination.exists():
        return destination

    counter = 1

    while True:
        new_name = f"{destination.stem}_{counter}{destination.suffix}"
        new_destination = destination.with_name(new_name)

        if not new_destination.exists():
            return new_destination

        counter += 1

def organize_files(directory, dry_run=False):
    path = Path(directory)

    for file in path.iterdir():
        if not file.is_file():
            continue

        category = get_category(file)
        destination = path / category / file.name
        destination = get_unique_destination(destination)

        print(f"{file.name} -> {destination}")

        if not dry_run:
            shutil.move(file, destination)
