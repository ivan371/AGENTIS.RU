from django import forms

class MediaModel(forms.Form):
	media_file = forms.ImageField()
