from django import forms
class EmailSendForm(forms.Form):
    to=forms.EmailField()