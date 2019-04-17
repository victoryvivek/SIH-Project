from django.urls import path
from . import views

app_name='first_app'
urlpatterns=[
    path('startupregistration/',views.startupRegistration,name='startupRegistration'),
    path('capitalistregistration/', views.capitalistRegistration,name='capitalistRegistration'),
    path('login/', views.login, name='login'),
    path('<int:choice>/<int:id>/afterlogin/', views.after_login, name='after_login'),
]
