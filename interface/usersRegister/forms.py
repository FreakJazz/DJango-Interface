from django import forms
from .models import Users

class registerForm(forms.ModelForm):
    class Meta: 
        model = Users
        fields = [
            'Name',
            'Username',
            'Phone',
            'Email',
            'Password',
        ]

        print(fields)
