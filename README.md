# File Organizer

一个使用 Python 编写的命令行文件整理工具。

根据文件扩展名，将文件自动整理到不同目录。

## Features

* 自动分类图片、文档、音乐、视频
* 未知文件归类到 `Others`
* 自动处理重复文件名
* 支持 `--dry-run` 预览
* pytest 自动化测试

## Project Structure

```text
file-organizer/
├── fileorganizer/
│   ├── __init__.py
│   └── organizer.py
├── tests/
│   └── test_filetool.py
├── filetool.py
└── README.md
```

## Usage

整理目录：

```bash
python filetool.py Downloads
```

预览整理结果：

```bash
python filetool.py Downloads --dry-run
```

查看帮助：

```bash
python filetool.py --help
```

例如：

```text
Downloads/
├── photo.jpg
├── report.pdf
├── song.mp3
└── video.mp4
```

整理后：

```text
Downloads/
├── Images/
│   └── photo.jpg
├── Documents/
│   └── report.pdf
├── Music/
│   └── song.mp3
└── Videos/
    └── video.mp4
```

## Supported Types

| Type      | Extensions          |
| --------- | ------------------- |
| Images    | jpg, jpeg, png, gif |
| Documents | pdf, doc, docx, txt |
| Music     | mp3, wav, flac      |
| Videos    | mp4, mkv, avi       |
| Others    | Other files         |

## Testing

```bash
python -m pytest
```

## Requirements

* Python 3.10+
* pytest

