from django.shortcuts import render,redirect
from .forms import *
from django.contrib import messages
from firstapp.models import *

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

def login(request):
    if request.method == 'POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            choice=form.cleaned_data['choice']
            if choice=='1':
                curuser=OrganisationInfo.objects.all().filter(username=username,password=password)
                if curuser:
                    list_id = curuser.values('id');
                    return redirect('first_app:after_login',choice=choice,id=list_id[0]['id'])
                else:
                    messages.error(request, 'Incorrect Username or Password')
            else:
                curuser = CapitalistInfo.objects.all().filter(username=username, password=password)
                if curuser:
                    list_id = curuser.values('id')
                    return redirect('first_app:after_login', id=list_id[0]['id'], choice=choice )
                else:
                    messages.error(request, 'Incorrect Username or Password')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def after_login(request,choice,id):
    print("After login")
    if choice==1:
        return render(request,'after_org_login.html',{'id':id})
    else:
        return render(request,'after_vc_login.html',{'id':id})
    
