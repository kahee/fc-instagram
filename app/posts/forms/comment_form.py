from django import forms

from ..models import Comment


class CommentModelForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'content',
        ]

        widgets = {
            'content': forms.TextInput(
                attrs={
                    'class': ('form-control', 'float-left', 'form-control',),
                    'style': 'width:90%',
                }
            )
        }
