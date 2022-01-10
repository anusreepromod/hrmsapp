from django.db import models

# Create your models here.


class department(models.Model):
    department_name = models.CharField(max_length=40)
    status = models.CharField(max_length=30, default=None, null=True)


class designation(models.Model):
    designation_name = models.CharField(max_length=40)
    department_id = models.ForeignKey(department, on_delete=models.CASCADE)
    status = models.CharField(max_length=30, default=None, null=True)


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
    salary = models.CharField(max_length=50)
    status = models.CharField(max_length=30)


class login(models.Model):
    username = models.EmailField()
    password = models.CharField(max_length=20)
    user_id = models.ForeignKey(employeedetail, on_delete=models.CASCADE)


class adminlogin(models.Model):
    username = models.EmailField()
    password = models.CharField(max_length=20)


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
    status = models.CharField(max_length=30, default=None, null=True)


class meeting(models.Model):
    mtitle = models.CharField(max_length=40)
    mdate = models.CharField(max_length=40)
    mtime = models.CharField(max_length=40)
    agenda = models.CharField(max_length=60)
    status = models.CharField(max_length=30, default=None, null=True)


class leavetype(models.Model):
    leavetype = models.CharField(max_length=40)
    status = models.CharField(max_length=30, default=None, null=True)


class resignation(models.Model):
    employeename = models.CharField(max_length=40)
    resignationdate = models.CharField(max_length=40)
    noticeperiod = models.CharField(max_length=40)
    description = models.CharField(max_length=60)
    employeeid = models.ForeignKey(employeedetail, on_delete=models.CASCADE)
    status = models.CharField(max_length=30, default=None, null=True)


class promotion(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=40)
    designation = models.CharField(max_length=40)
    promotiontitle = models.CharField(max_length=40)
    promotiondate = models.CharField(max_length=40)
    remarks = models.CharField(max_length=40)
    employeeid = models.ForeignKey(employeedetail, on_delete=models.CASCADE)
    status = models.CharField(max_length=30, default=None, null=True)


class leave(models.Model):
    employeename = models.CharField(max_length=50)
    startdate = models.CharField(max_length=40)
    enddate = models.CharField(max_length=40)
    reason = models.CharField(max_length=40)
    remark = models.CharField(max_length=40)
    employeeid = models.ForeignKey(employeedetail, on_delete=models.CASCADE)
    leavecategory = models.ForeignKey(leavetype, on_delete=models.CASCADE)
    status = models.CharField(max_length=30)


class notification(models.Model):
    notify = models.CharField(max_length=500)


class allowance(models.Model):
    allowancetype = models.CharField(max_length=50)
    amount = models.CharField(max_length=40)


class payroll(models.Model):
    salary = models.CharField(max_length=40)
    basic = models.CharField(max_length=40)
    hra = models.CharField(max_length=40)
    specialallowance = models.CharField(max_length=40)
    medicalallowance = models.CharField(max_length=40)
    conveyance = models.CharField(max_length=40)
    grossearning = models.CharField(max_length=40)
    ptax = models.CharField(max_length=40)
    tds = models.CharField(max_length=40)
    grossdeduction = models.CharField(max_length=40)
    netpay = models.CharField(max_length=40)


class holiday(models.Model):
    day = models.CharField(max_length=40)
    date = models.CharField(max_length=40)
    occassion = models.CharField(max_length=40)
    holidaytype = models.CharField(max_length=40)
    status = models.CharField(max_length=40)
