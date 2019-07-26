from django import forms

class Emailform(forms.Form):
    name = forms.CharField(label = 'name', max_length = '30')
    emailid = forms.CharField(label = 'emailid', max_length = '50')
    subject = forms.CharField(label = 'subject', max_length = '100')
    comment = forms.CharField(label = 'comment', max_length = '1000')