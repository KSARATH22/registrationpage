from django.db import models
class RegistrationData(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    mobaile=models.BigIntegerField()
    email=models.EmailField(max_length=50)
    # date=models.DateField(max_length=50)
    username=models.CharField(max_length=50)
    password1=models.CharField(max_length=50)
    password2=models.CharField(max_length=50)

