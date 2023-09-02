from django import forms
from .models import Blog
from django_editorjs import EditorJsField


class TextForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea, required=True)


class AddBlogForm(forms.ModelForm):
    description = EditorJsField() # Rich text alanı olarak tanımla

    class Meta:
        model = Blog
        fields = (
            "title",
            "category",
            "banner",
            "description"
        )
