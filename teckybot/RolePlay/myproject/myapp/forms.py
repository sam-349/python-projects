from django import forms


class SessionForm(forms.Form):
    username = forms.CharField(max_length=100, label="Username")
    role = forms.CharField(max_length=100, label="Role")
    experience = forms.IntegerField(min_value=0, label="Years of Experience")
