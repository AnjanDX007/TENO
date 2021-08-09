from django.db import models
from django.contrib.auth.models import User,PermissionsMixin
# Create your models here.
class User(models.Model):
    Account_number=models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    email_id=models.EmailField(max_length=100)
    phone_NO=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    Balance=models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Transfers(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    transfer_amount=models.IntegerField()
    transfer_date=models.DateField()
    transfer_time=models.TimeField()

    def __str__(self):
        return self.transfer_date + "\t " + self.transfer_time
