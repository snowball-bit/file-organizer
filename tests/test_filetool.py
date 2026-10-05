from pathlib import Path

from fileorganizer.organizer import (
    create_category_dirs,
    get_category,
    get_unique_destination,
    organize_files,
)

from filetool import main

def test_get_category_image():
    file = Path("photo.jpg")

    assert get_category(file) == "Images"


def test_get_category_document():
    file = Path("report.pdf")

    assert get_category(file) == "Documents"


def test_get_category_music():
    file = Path("song.mp3")

    assert get_category(file) == "Music"


def test_get_category_video():
    file = Path("movie.mp4")

    assert get_category(file) == "Videos"


def test_get_category_unknown():
    file = Path("program.xyz")

    assert get_category(file) == "Others"


def test_organize_files(tmp_path):
    photo = tmp_path / "photo.jpg"
    photo.write_text("test")

    create_category_dirs(tmp_path)
    organize_files(tmp_path)

    assert not photo.exists()
    assert (tmp_path / "Images" / "photo.jpg").exists()


def test_duplicate_filename(tmp_path):
    images = tmp_path / "Images"
    images.mkdir()

    old_photo = images / "photo.jpg"
    old_photo.write_text("old")

    new_photo = tmp_path / "photo.jpg"
    new_photo.write_text("new")

    create_category_dirs(tmp_path)
    organize_files(tmp_path)

    assert old_photo.exists()
    assert (images / "photo_1.jpg").exists()


def test_get_unique_destination(tmp_path):
    destination = tmp_path / "photo.jpg"

    destination.write_text("old")

    new_destination = get_unique_destination(destination)

    assert new_destination == tmp_path / "photo_1.jpg"

def test_get_unique_destination_multiple_duplicates(tmp_path):
    destination = tmp_path / "photo.jpg"

    destination.write_text("0")
    (tmp_path / "photo_1.jpg").write_text("1")
    (tmp_path / "photo_2.jpg").write_text("2")

    new_destination = get_unique_destination(destination)

    assert new_destination == tmp_path / "photo_3.jpg"

def test_organize_files_ignores_directories(tmp_path):
    images = tmp_path / "Images"
    images.mkdir()

    photo = tmp_path / "photo.jpg"
    photo.write_text("test")

    create_category_dirs(tmp_path)
    organize_files(tmp_path)

    assert (tmp_path / "Images" / "photo.jpg").exists()
    assert images.is_dir()

def test_get_category_uppercase_extension():
    file = Path("PHOTO.JPG")

    assert get_category(file) == "Images"

def test_get_category_no_extension():
    file = Path("README")

    assert get_category(file) == "Others"

def test_main_invalid_directory(monkeypatch):
    monkeypatch.setattr(
        "sys.argv",
        ["filetool.py", "not_exist"],
    )

    assert main() == 1

def test_main_success(tmp_path, monkeypatch):
    photo = tmp_path / "photo.jpg"
    photo.write_text("test")

    monkeypatch.setattr(
        "sys.argv",
        ["filetool.py", str(tmp_path)],
    )

    assert main() == 0
    assert (tmp_path / "Images" / "photo.jpg").exists()

def test_organize_files_dry_run(tmp_path):
    photo = tmp_path / "photo.jpg"
    photo.write_text("test")

    create_category_dirs(tmp_path)
    organize_files(tmp_path, dry_run=True)

    assert photo.exists()
    assert not (tmp_path / "Images" / "photo.jpg").exists()
