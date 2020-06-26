from django import forms
from .models import Members, Courses

class MembershipForm(forms.ModelForm):
    class Meta:
        model = Members
        fields = ['firstname', 'lastname', 'email', 'studentID', 'subject', 'year']

        widgets = {
            'firstname': forms.TextInput(attrs={'class':'form-control'}),
            'lastname': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'studentID': forms.TextInput(attrs={'class':'form-control'}),
            'subject': forms.Select(attrs={'class':'form-control'}),
            'year': forms.TextInput(attrs={'class':'form-control'})
        }
