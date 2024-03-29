# Kanji
Simple temporary file hosting solution, powered by Django.

Page design based on [Uguu](https://github.com/nokonoko/uguu).

## Installation

Please install Python 3.x and pip if you don't have them already.

First install the dependencies:
```bash
sudo pip3 install django django-qr-code python-magic
```
Start the server:
```bash
git clone https://github.com/izq/kanji.git
unzip kanji.git
cd kanji
python3 manage.py migrate --run-syncdb
python3 manage.py runserver
```
And setup a cron job (_crontab -e_) to delete uploaded files older than 24 hours :
```bash
*/5 * * * * root /home/izq/kanji/check.sh
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

## Screenshot
![Screenshot](https://raw.githubusercontent.com/izq/kanji/master/screenshot.png)
