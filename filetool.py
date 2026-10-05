import argparse

from fileorganizer.organizer import (
    create_category_dirs,
    organize_files,
    validate_directory,
)


def parse_args():
    parser = argparse.ArgumentParser(
        description="Organize files by type"
    )

    parser.add_argument(
        "directory",
        help="Directory to organize"
    )

    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview changes without moving files"
    )

    return parser.parse_args()


def main():
    args = parse_args()

    if not validate_directory(args.directory):
        return 1

    if not args.dry_run:
        create_category_dirs(args.directory)

    organize_files(
        args.directory,
        dry_run=args.dry_run,
    )

    return 0


if __name__ == "__main__":
    exit(main())
