from django import forms
from .models import *

class OrganisationInfoForm(forms.ModelForm):
    class Meta:
        model=OrganisationInfo
        fields='__all__'


class CapitalistInfoForm(forms.ModelForm):
    class Meta:
        model = CapitalistInfo
        fields = '__all__'

#class LoginForm(forms.Form):

