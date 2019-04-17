from django.shortcuts import render
from .forms import *

def startupRegistration(request):
    if request.method=='POST':
        form = OrganisationInfoForm(request.POST)
        if form.is_valid():
            form.save(commit=True);
            return render(request, 'org_registration.html', {'form': form})
    else:
        form=OrganisationInfoForm()
        return render(request, 'org_registration.html', {'form': form})

def capitalistRegistration(request):
    if request.method == 'POST':
        form = CapitalistInfoForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return render(request, 'vc_registration.html', {'form': form})
    else:
        form = CapitalistInfoForm()
        return render(request, 'vc_registration.html', {'form': form})


