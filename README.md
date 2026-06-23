# 📖 Audio Book Reader

A simple Python app that converts any PDF into an audiobook. Select a PDF file through a file dialog and the app will read it aloud page by page using text-to-speech.

## Features

- Browse and select any PDF file using a file picker dialog
- Extracts text from each page automatically
- Reads the text aloud using your system's text-to-speech engine

## Requirements

- Python 3.x
- [pyttsx3](https://pypi.org/project/pyttsx3/)
- [PyPDF2](https://pypi.org/project/PyPDF2/)
- tkinter (included with Python by default)

## Installation

```bash
pip install pyttsx3 PyPDF2
```

## Usage

```bash
python main.py
```

A file dialog will open — select any PDF file and the app will begin reading it aloud from the first page.

## Notes

- Works offline — no internet connection required
- Uses your operating system's built-in TTS voices
- Best suited for text-based PDFs; scanned image PDFs may not extract text correctly
