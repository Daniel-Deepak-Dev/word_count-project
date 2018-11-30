from django import forms

class exampleform(forms.Form):

    typed_text = forms.CharField(widget=forms.Textarea())