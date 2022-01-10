from django.db import models

# Create your models here.


class workinghours(models.Model):
    employeeid = models.BigIntegerField()
    employeename = models.CharField(max_length=30)
    date = models.DateField()
    checkin = models.TimeField()
    checkout = models.TimeField(default=None, null=True)
    totalhours = models.TimeField(default=None, null=True)
