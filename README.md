# Kanji
Simple file uploading and sharing website, powered by Django

## Installation

Please install Python 3.x and pip if you don't have them already.

First install the dependencies:
```bash
sudo pip3 install django django-qr-code python-magic
```
Then run the server:
```bash
git clone https://github.com/izq/kanji.git
unzip kanji.git
cd kanji
python3 manage.py runserver
```

## Configuration
Most of the variables you may want to customize are located in _/kanji/settings.py_
```python
BANNED_MIMETYPES = ["text/html", "application/x-msdownload", "application/x-ms-installer", "application/x-elf"]

MAX_SIZE = 104857600

WEBSITE_ROOT = "http://127.0.0.1:8000"
```
**_MAX_SIZE_** is the maximum file size, i.e 100MB.

**_WEBSITE_ROOT_** is the domain name used to generate the URL that is returned to the user.
