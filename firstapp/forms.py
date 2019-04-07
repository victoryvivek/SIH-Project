from django import forms
from .models import *

class OrganisationInfoForm(forms.ModelForm):
    class Meta:
        model=OrganisationInfo
        fields='__all__'
