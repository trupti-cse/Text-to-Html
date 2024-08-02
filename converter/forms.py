from django import forms
from ckeditor.widgets import CKEditorWidget
from .models import History

class PostForm(forms.ModelForm):
    body = forms.CharField(widget=CKEditorWidget(), label="Text Editor")

    class Meta:
        model = History
        fields = ('body',)
