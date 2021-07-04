from django import forms


class reg_info(forms.Form):
    name = forms.CharField(label="নাম", min_length=2, widget=forms.TextInput({"class": "input", "placeholder": "তোমার নাম"}))
    email = forms.EmailField(label="ইমেইল", widget=forms.TextInput({"class": "input", "placeholder": "তোমার ইমেইল"}))
    phone = forms.RegexField(label="ফোন নম্বর", regex=r'^017', widget=forms.TextInput({"class": "input", "placeholder": "তোমার মোবাইল নম্বর"}))
    agree = forms.BooleanField(label="")
