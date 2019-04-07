from django.urls import path
from . import views

urlpatterns=[
    path('startupregistration/',views.startupRegistration,name='startupRegistration'),
]