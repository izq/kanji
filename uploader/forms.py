from django import forms
from . import models
from django.conf import settings as conf

class DocumentForm(forms.ModelForm):

    class Meta:
        model = models.Document
        fields = ('file','randomname','customname')

    file = forms.FileField(required=True)
    randomname = forms.BooleanField(required=False)
    customname = forms.CharField(max_length=50, required=False, error_messages={'max_length': 'The custom filename is limited to 50 characters, sorry about that.'})

    def clean_file(self):
        file = self.cleaned_data['file']
        if file.content_type in conf.BANNED_MIMETYPES:
            raise forms.ValidationError("File type not allowed, sorry about that.")
        elif file.size > conf.MAX_SIZE:
            raise forms.ValidationError("The maximum file size allowed is 100MB, sorry about that.")
        return file
