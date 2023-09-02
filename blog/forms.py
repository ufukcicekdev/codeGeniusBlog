from django import forms
from .models import Blog
from django_editorjs import EditorJsField


class TextForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea, required=True)


class AddBlogForm(forms.ModelForm):
    description = EditorJsField(
        editorjs_config={
            "tools":{
                "Link":{
                    "config":{
                        "endpoint":
                            '/linkfetching/'
                        }
                },
                "Image":{
                    "config":{
                        "endpoints":{
                            "byFile":'/uploadi/',
                            #"byUrl":'uploadi/'
                        }
                    }
                },
                "Attaches":{
                    "config":{
                        "endpoint":'/uploadf/'
                    }
                }
            }
        }
    ) # Rich text alanı olarak tanımla

    class Meta:
        model = Blog
        fields = (
            "title",
            "category",
            "banner",
            "description"
        )
