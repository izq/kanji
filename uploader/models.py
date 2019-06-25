from django.db import models
import os
import random
import string

def randomix():
	return ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(5))

def content_file_name(instance, filename):
    if instance.randomname == True:
        ext = filename.split('.')[-1]
        filename = randomix() + "." + ext
    elif instance.customname != "":
        filename = randomix() + "_" + instance.customname
    else:
        filename = randomix() + "_" + instance.file.name

    return os.path.join('', filename)

class Document(models.Model):
    file = models.FileField(upload_to=content_file_name)
    randomname = models.BooleanField()
    customname = models.CharField(max_length=50)
    uploaded_at = models.DateTimeField(auto_now_add=True)
