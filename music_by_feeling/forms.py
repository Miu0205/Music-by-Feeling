from django import forms

from .models import Comment, Music


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)


class MusicForm(forms.ModelForm):
    class Meta:
        model = Music
        fields = ('feeling_1','feeling_2','artist','genre', 'era', 'famous')
