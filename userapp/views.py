from django.http.response import JsonResponse
from django.shortcuts import render
from adminapp.models import *
from userapp.models import *
from adminapp.models import *
from datetime import datetime
import datetime as dt

# Create your views here.


def fnlogin(request):
    try:
        if request.method == 'POST':
            username = request.POST['username']
            print(username)
            password = request.POST['password']
            print(password)
            logi_obj = login.objects.get(username=username, password=password)
            print(logi_obj.id)
            request.session['log'] = logi_obj.id
            print(request.session['log'])
            log_obj = employeedetail.objects.get(id=logi_obj.user_id_id)
            return render(request, 'dashboard.html', {'username': log_obj})
    except Exception as e:
        print(e)

    return render(request, 'login.html')


# def master(request):
#     logid = request.session['log']
#     log_obj = employeedetail.objects.get(id=logid)
#     notify = notification.objects.all()
#     return render(request, 'master.html', {'username': log_obj, 'notify': notify.id})
def master(request):

    logid = request.session.get('log')

    print(logid)

    logi = login.objects.get(id=logid)

    notify = notification.objects.all().count()

    return JsonResponse({'user': logi.username,  'notify': notify})


def getdatas(request):
    logid = request.session.get('log')
    print(logid)
    user = employeedetail.objects.get(id=logid)
    holidays = holiday.objects.all().count()
    l_obj = leavetype.objects.all()
    list = []
    for i in l_obj:
        list.append(i.id)
    sick = leave.objects.filter(
        employeeid=logid, leavecategory=list[0]).count()
    sicks = 6-sick
    casual = leave.objects.filter(
        employeeid=logid, leavecategory=list[1]).count()
    casuals = 12-casual
    print(holidays)

    return JsonResponse({'salary': user.salary, 'holiday': holidays, 'sick': sicks, 'casual': casuals})


def getuserprofile(request):
    logid = request.session['log']
    print(logid)
    log_obj = employeedetail.objects.filter(
        id=logid).select_related('department_id', 'designation_id')
    print(log_obj)
    c_obj = contactdetails.objects.filter(id=logid)
    print(c_obj)
    edetails = [{'name': i.firstname, 'mname': i.middlename, 'lname': i.lastname, 'dob': i.date, 'fname': i.fathersname, 'gender': i.gender, 'mstatus': i.maritalstatus,
                 'etype': i.employeetype, 'dept': i.department_id.department_name, 'des': i.designation_id.designation_name, 'grade': i.employeegrade, 'doj': i.doj, 'shift': i.shift}for i in log_obj]
    contact = [{'pemail': i.personalemail, 'address': i.address, 'city': i.city, 'country': i.country,
                'pincode': i.pincode, 'mobile': i.mobile} for i in c_obj]

    print(contact)
    return JsonResponse({'edetails': edetails, 'cdetails': contact})


def fnlogout(request):
    del request.session['log']
    return render(request, 'login.html')


def dashboard(request):
    return render(request, 'dashboard.html')


def editprofile(request):
    try:
        logid = request.session['log']
        pemail = request.POST['pemail']
        print(pemail)
        address = request.POST['address']
        print(address)
        city = request.POST['city']
        print(city)
        country = request.POST['country']
        print(country)
        pincode = request.POST['pincode']
        print(pincode)
        mobile = request.POST['mobile']
        print(mobile)
        contactdetails.objects.filter(id=logid).update(personalemail=pemail,
                                                       address=address, city=city, country=country, pincode=pincode, mobile=mobile)

        return render(request, 'editprofile.html', )
    except Exception as e:
        print(e)
    ed_obj = employeedetail.objects.get(id=logid)
    e_obj = login.objects.get(user_id_id=logid)
    c_obj = contactdetails.objects.get(id=logid)
    return render(request, 'editprofile.html', {'emp': ed_obj, 'email': e_obj, 'contact': c_obj, 'msg': 'Data updated'})


def leaves(request):
    return render(request, 'leaveapplication.html')


def applyleave(request):
    try:
        cpass = request.session['log']
        print(cpass)
        if request.method == 'POST':
            empname = request.POST['empname']
            empid = request.POST['empid']
            lcategory = request.POST['lcategory']
            startdate = request.POST['startdate']
            enddate = request.POST['enddate']
            lreason = request.POST['lreason']
            remark = request.POST['remark']
            cleave_obj = leave(employeename=empname, leavecategory_id=lcategory, startdate=startdate,
                               enddate=enddate, reason=lreason, remark=remark, employeeid_id=empid)
            print(cleave_obj)
            cleave_obj.save()
            return render(request, 'applyleave.html', {'msg': "Data inserted successfully"})
    except Exception as e:
        print(e)
    leave_obj = leavetype.objects.all()
    user = employeedetail.objects.get(id=cpass)
    return render(request, 'applyleave.html', {'leave': leave_obj, 'user': user})


def notifications(request):
    notify = notification.objects.all()
    return render(request, 'notification.html', {'notify': notify})


def leavedetail(request):
    return render(request, 'leavedetail.html')


def fnleave(request):
    try:
        logid = request.session['log']

        leaves = leave.objects.filter(
            employeeid_id=logid).select_related('leavecategory')

        leave_obj = [{'id': i.id, 'emp': i.employeename, 'empid': i.employeeid_id, 'lc': i.leavecategory.leavetype, 'sd': i.startdate,
                      'ed': i.enddate, 'reason': i.reason, 'remarks': i.remark, 'status': i.status} for i in leaves]

        print(leave_obj)
        return JsonResponse({'leave': leave_obj})
    except Exception as e:
        print(e)
    return render(request, 'leaveapplication.html')


def userprofile(request):
    return render(request, 'userprofile.html')


def settings(request):
    try:
        cpass = request.session['log']
        print(cpass)
        cpass_obj = login.objects.get(id=cpass)
        opassword = request.POST['opassword']
        print(opassword)
        npassword = request.POST['newpassword']
        if cpass_obj.password == opassword:
            cpass_obj.password = npassword
            cpass_obj.save()
            return render(request, 'settings.html', {'msg': 'password changed successfully'})
    except Exception as e:
        print(e)
    return render(request, 'settings.html')


def attendance(request):
    return render(request, 'attendance.html')


def fnattendance(request):
    logid = request.session['log']
    print(logid)
    attend = workinghours.objects.filter(employeeid=logid)
    attendance = [{'id': i.id, 'date': i.date, 'checkin': i.checkin,
                   'checkout': i.checkout, 'th': i.totalhours} for i in attend]
    print(attendance)
    return JsonResponse({'attendance': attendance})


def holidays(request):
    return render(request, 'holidaylist.html')


def fncheckin(request):
    if request.method == 'POST':
        logid = request.session['log']
        print(logid)
        date = request.POST['date']
        print(date)
        time = request.POST['time']
        print(time)
        emp = employeedetail.objects.get(id=logid)
        empname = emp.firstname
        print(empname)
        checkid = workinghours(
            employeeid=logid, employeename=empname, date=date, checkin=time)
        checkid.save()
        request.session['check'] = checkid.id
        print(checkid.id)
        return JsonResponse({'msg': "Saved Successfully"})
    return render(request, 'dashboard.html', {'msg': "Welcome"})


def fncheckout(request):
    if request.method == 'POST':
        logid = request.session['check']
        print(logid)
        time1 = request.POST['time']
        workinghours.objects.filter(
            id=logid).update(checkout=time1)
        total_obj = workinghours.objects.get(id=logid)
        date1 = total_obj.date
        checkin = total_obj.checkin
        print(checkin)
        checkout = total_obj.checkout
        print(checkout)
        combined = datetime.combine(date1, checkin)
        combined1 = datetime.combine(date1, checkout)
        total = combined1-combined
        t = str(total)
        print(total)
        workinghours.objects.filter(
            id=logid).update(totalhours=t)
        return JsonResponse({'msg': "You have been checked out"})
    return render(request, 'dashboard.html', {'msg': "data not saved"})


def getmeeting(request):
    meet = meeting.objects.all()
    meet_obj = [{'id': i.id, 'mt': i.mtitle, 'md': i.mdate,
                 'time': i.mtime, 'agenda': i.agenda} for i in meet]
    return JsonResponse({'meet': meet_obj})


def resignations(request):
    return render(request, 'resignations.html')


def addresignation(request):
    cpass = request.session['log']
    print(cpass)
    if request.method == 'POST':
        empid = request.POST['employeeid']
        print(empid)
        empname = request.POST['employeename']
        print(empname)
        resdate = request.POST['resignationdate']
        print(resdate)
        np = request.POST['noticeperiod']
        print(np)
        desc = request.POST['description']
        print(desc)
        status = 'none'
        resignation_obj = resignation(employeename=empname,
                                      resignationdate=resdate, noticeperiod=np, description=desc, employeeid_id=empid, status=status)
        resignation_obj.save()
        print(resignation_obj)

        return render(request, 'addresignation.html', {'msg': "Data inserted"})
    # except Exception as e:
    #     print(e)
    user = employeedetail.objects.get(id=cpass)
    return render(request, 'addresignation.html', {'user': user})


def fnresignations(request):
    resid = request.session['log']
    print(resid)
    resign = resignation.objects.get(employeeid_id=resid)
    resign_obj = [{'id': resign.id, 'empid': resign.employeeid_id, 'employeename': resign.employeename, 'resignationdate': resign.resignationdate, 'noticeperiod': resign.noticeperiod,
                   'description': resign.description, 'status': resign.status}]
    print(resign_obj)
    return JsonResponse({'resign': resign_obj})


def getresignation(request):
    try:
        if request.method == 'POST':
            resid = request.session['log']
            print(resid)
            resignation_obj = resignation.objects.get(id=resid)
            res_obj = [{'id': resignation_obj.id, 'empid': resignation_obj.employeeid_id, 'empname': resignation_obj.employeename,
                        'resdate': resignation_obj.resignationdate, 'np': resignation_obj.noticeperiod, 'desc': resignation_obj.description}]
            print(res_obj)
            return JsonResponse({'res': res_obj})
    except Exception as e:
        print(e)


def updateresignation(request):
    try:
        if request.method == 'POST':
            id = request.POST['id']
            print(id)
            empid = request.POST['empid']
            print(empid)
            empname = request.POST['empname']
            print(empname)
            resdate = request.POST['resdate']
            print(resdate)
            np = request.POST['np']
            print(np)
            desc = request.POST['desc']
            print(desc)
            resignation.objects.filter(id=id).update(employeename=empname,
                                                     resignationdate=resdate, noticeperiod=np, description=desc, employeeid_id=empid)
            return JsonResponse({'msg': 'Data updated successfully'})
    except Exception as e:
        print(e)
