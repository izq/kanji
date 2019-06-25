# setup a cron job to run the script automatically:
# */5 * * * * root /home/izq/kanji/check.sh
find ./uploader/media/ -type f -mtime +1 -delete
