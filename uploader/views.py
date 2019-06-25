from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.views.static import serve
from django.conf import settings as conf
from django.utils.encoding import smart_str
import magic

import os
from . import forms

def index(request):
    if request.method == 'POST':
        form = forms.DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            f = form.save()
            path = conf.WEBSITE_ROOT + "/" + str(f.file)
            return render(request, "index.html", {"uploaded_file_url":path})
        else:
            return render(request, "index.html", {"errors":form.errors})
    return render(request, "index.html")

def info(request):
    return render(request, "index.html", {"info":"True"})
    
def fileserve(request, id):
    try:
        with open(conf.MEDIA_URL+id, 'rb') as f:

			#read the file we will return
            file_data = f.read()

            #we don't need to pass the whole file to magic to detect the mime type
            f.seek(0)
            mime_type = magic.from_buffer(f.read(30), mime=True)


            # sending response 
            response = HttpResponse(file_data, content_type='%s; charset=utf-8' % mime_type)

    except IOError:
        # if the file doesn't exist
        return render(request, "notfound.html")

    return response
