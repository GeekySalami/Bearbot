from django import forms
from django.utils.safestring import SafeString

class codeareaform(forms.Form):
	code = forms.CharField(label ='', required = False)
	fields=['code']

	def as_div(self):
		return SafeString(super().as_div().replace('<div>', '<div id="editor">'))
