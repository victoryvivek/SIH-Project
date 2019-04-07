from django.db import models


# Create your models here.
class OrganisationInfo(models.Model):
    orgnisation_name=models.CharField(max_length=30)
    username=models.CharField(max_length=150)
    password=models.CharField(max_length=150)
    email=models.EmailField()
    contact_no=models.DecimalField(max_digits=10,decimal_places=0)
    org_domain=models.CharField(max_length=150)

    def __str__(self):
        return self.orgnisation_name



