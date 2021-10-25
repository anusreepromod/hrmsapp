from django.db import models

# Create your models here.


class department(models.Model):
    department_name = models.CharField(max_length=40)


class designation(models.Model):
    designation_name = models.CharField(max_length=40)
    department_id = models.ForeignKey(department, on_delete=models.CASCADE)


class employeedetail(models.Model):
    firstname = models.CharField(max_length=30)
    middlename = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    email = models.EmailField()
    date = models.DateField()
    gender = models.CharField(max_length=10)
    fathersname = models.CharField(max_length=30)
    maritalstatus = models.CharField(max_length=30)
    employeetype = models.CharField(max_length=30)
    department_id = models.ForeignKey(department, on_delete=models.CASCADE)
    designation_id = models.ForeignKey(designation, on_delete=models.CASCADE)
    doj = models.DateField()
    employeegrade = models.CharField(max_length=30)
    shift = models.CharField(max_length=30)


class login(models.Model):
    username = models.EmailField()
    password = models.CharField(max_length=20)
    user_id = models.ForeignKey(employeedetail, on_delete=models.CASCADE)


class contactdetails(models.Model):
    personalemail = models.CharField(max_length=30)
    address = models.CharField(max_length=60)
    city = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    pincode = models.IntegerField()
    mobile = models.BigIntegerField()
    personal_id = models.ForeignKey(employeedetail, on_delete=models.CASCADE)


class document(models.Model):
    certificate = models.CharField(max_length=100)
    resume = models.CharField(max_length=100)
    photo = models.CharField(max_length=100)
    personal_id = models.ForeignKey(
        employeedetail, on_delete=models.CASCADE, default=None)


class complaint(models.Model):
    cf = models.CharField(max_length=30)
    ca = models.CharField(max_length=30)
    title = models.CharField(max_length=40)
    doc = models.DateField()
    description = models.CharField(max_length=100)


class meeting(models.Model):
    mtitle = models.CharField(max_length=40)
    mdate = models.CharField(max_length=40)
    mtime = models.CharField(max_length=40)
    agenda = models.CharField(max_length=60)


class leavetype(models.Model):
    leavetype = models.CharField(max_length=40)
