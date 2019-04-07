from django.shortcuts import render
from .models import *
from .forms import OrganisationInfoForm

def startupRegistration(request):
    if request.method=='POST':
        form = OrganisationInfoForm(request.POST)
        if form.is_valid():
            return render(request, 'org_registration.html', {'form': form})
    else:
        form=OrganisationInfoForm()
        return render(request, 'org_registration.html', {'form': form})