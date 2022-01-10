from django.shortcuts import render

from django.conf import settings
from . models import *
# Create your views here.
from random import random
from django.core.files.storage import FileSystemStorage
from django.http.response import JsonResponse
from userapp.models import *
from django.core.mail import send_mail
from django.db.models import Q
from django.db.models import Count


def logins(request):
    try:
        if request.method == 'POST':
            username = request.POST['username']
            print(username)
            password = request.POST['password']
            print(password)
            logi_obj = adminlogin.objects.get(
                username=username, password=password)
            # print(logi_obj.id)
            request.session['log'] = logi_obj.id

            return render(request, 'dashboards.html')
    except Exception as e:
        print(e)
    return render(request, 'logins.html')


def masters(request):

    logid = request.session.get('log')

    print(logid)

    logi = adminlogin.objects.get(id=logid)

    notify = notification.objects.all().count()

    return JsonResponse({'user': logi.username, 'notify': notify})

    # return render(request, 'masters.html', {'username': logi, 'notify': notify})


def fnlogout(request):
    del request.session['log']
    return render(request, 'logins.html')


def addstaff(request):
    try:
        email = request.POST['email']
        print(email)
        u_obj = login.objects.filter(username=email).exists()
        print(u_obj)
        if u_obj == False:
            firstname = request.POST['firstname']
            print(firstname)
            middlename = request.POST['middlename']
            print(middlename)
            lastname = request.POST['lastname']
            print(lastname)
            password = request.POST['password']
            print(password)
            day = request.POST['day']
            print(day)
            month = request.POST['month']
            print(month)
            year = request.POST['years']
            print(year)
            date = year+'-'+month+'-'+day
            print(date)
            gender = request.POST['gender']
            print(gender)
            fathersname = request.POST['fathersname']
            print(fathersname)
            marital = request.POST['marital']
            print(marital)
            personalemail = request.POST['personalemail']
            print(personalemail)
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
            employeetype = request.POST['employeetype']
            print(employeetype)
            department_id = request.POST['department']
            print(department_id)
            designation_id = request.POST['designation']
            print(designation_id)
            days = request.POST['days']
            print(days)
            months = request.POST['months']
            print(months)
            years = request.POST['years']
            print(years)
            dates = years+'-'+months+'-'+days
            print(dates)
            employeegrade = request.POST['employeegrade']
            print(employeegrade)
            shift = request.POST['shift']
            print(shift)
            salary = request.POST['salary']
            print(salary)
            certificate = request.FILES['certificates']
            certificate_name = str(random())+certificate.name
            print(certificate_name)
            certificate_obj = FileSystemStorage()
            certificate_obj.save(certificate_name, certificate)
            resume = request.FILES['resume']
            resume_name = str(random())+resume.name
            print(resume_name)
            resume_obj = FileSystemStorage()
            resume_obj.save(resume_name, resume)
            photo = request.FILES['photo']
            photo_name = str(random())+photo.name
            print(photo_name)
            photo_obj = FileSystemStorage()
            photo_obj.save(photo_name, photo)
            status = 1
            user_obje = employeedetail(firstname=firstname, middlename=middlename, lastname=lastname,
                                       date=date, gender=gender, fathersname=fathersname, maritalstatus=marital, email=email, employeetype=employeetype, department_id_id=department_id, designation_id_id=designation_id,
                                       doj=dates, employeegrade=employeegrade, shift=shift, salary=salary, status=status)
            print(user_obje)
            user_obje.save()
            contact_obj = contactdetails(personalemail=personalemail, address=address, city=city,
                                         country=country, pincode=pincode, mobile=mobile, personal_id_id=user_obje.id)
            contact_obj.save()

            document_obj = document(
                certificate=certificate_name, resume=resume_name, photo=photo_name, personal_id_id=user_obje.id)
            document_obj.save()
            print(document_obj)
            login_obj = login(username=email, password=password,
                              user_id_id=user_obje.id)
            login_obj.save()

            return render(request, 'addstaff.html', {'message': 'User registered successfully'})
        else:
            return render(request, 'addstaff.html', {'msg': 'User already exist'})
    except Exception as e:
        print(e)
    department_obj = department.objects.all()
    designation_obj = designation.objects.all()
    print(department_obj)
    print(designation_obj)
    return render(request, 'addstaff.html', {'departments': department_obj, 'designations': designation_obj})


def editemployee(request):

    return render(request, 'editemployee.html',)


def employee(request):
    users_obje = employeedetail.objects.all()
    user_obj = [{'id': i.id, 'fname': i.firstname, 'email': i.email, 'department': i.department_id_id,
                 'designation': i.designation_id_id, 'doj': i.doj}for i in users_obje]
    return JsonResponse({'user': user_obj})


def employees(request):
    return render(request, 'employee.html')


def fnemployee(request):
    return render(request, 'employee.html')


def employeess(request):
    department_obj = department.objects.all()
    designation_obj = designation.objects.all()

    return render(request, 'employeess.html', {'department': department_obj, 'designation': designation_obj})


def searchemployee(request):
    search = request.POST['search']
    print(search)
    search_obj = employeedetail.objects.filter(Q(firstname=search) | Q(email=search)).select_related(
        'department_id', 'designation_id')
    print(search_obj)
    s_obj = [{'id': i.id, 'fname': i.firstname, 'email': i.email, 'department': i.department_id.department_name,
              'designation': i.designation_id.designation_name, 'doj': i.doj}for i in search_obj]
    print(s_obj)
    return JsonResponse({'user': s_obj})


def fnemployeess(request):
    # users_obje = employeedetail.objects.all()
    user_obje = employeedetail.objects.select_related(
        'department_id', 'designation_id')
    # for i in user_obj:
    #     print(i.department_id.department_name)
    #     print(i.designation_id.designation_name)
    user_obj = [{'id': i.id, 'fname': i.firstname, 'email': i.email, 'department': i.department_id.department_name,
                 'designation': i.designation_id.designation_name, 'doj': i.doj}for i in user_obje]
    return JsonResponse({'user': user_obj})


def fneditemployee(request):
    if request.method == 'POST':
        emp = request.POST['uid']
        print(emp)
        emp_obj = employeedetail.objects.get(id=emp)
        print(emp_obj)
        off_obj = contactdetails.object.get(personal_id_id=emp)
        print(off_obj)
        emp_obj = [{'id': emp_obj.id, 'fname': emp_obj.firstname,
                    'pemail': off_obj.personalemail}]

    return JsonResponse({'data': emp_obj})


def getdata(request):
    try:
        if request.method == 'POST':
            emp = request.POST['uid']
            print(emp)
        emp_obj = employeedetail.objects.get(id=emp)
        print(emp_obj)
        log_obj = login.objects.get(user_id_id=emp)
        per_obj = contactdetails.objects.get(personal_id_id=emp)
        doc = document.objects.get(personal_id_id=emp)
        print(per_obj)
        emp_obj1 = [{'id': emp_obj.id, 'fname': emp_obj.firstname, 'mname': emp_obj.middlename, 'lname': emp_obj.lastname, 'gender': emp_obj.gender, 'email': emp_obj.email, 'password': log_obj.password, 'date': emp_obj.date, 'fathersname': emp_obj.fathersname, 'mstatus': emp_obj.maritalstatus, 'doj': emp_obj.doj,
                     'emptype': emp_obj.employeetype, 'empgrade': emp_obj.employeegrade, 'shift': emp_obj.shift, 'department': emp_obj.department_id_id, 'designation': emp_obj.designation_id_id, 'pemail': per_obj.personalemail, 'address': per_obj.address, 'city': per_obj.city, 'country': per_obj.country, 'pincode': per_obj.pincode, 'mobile': per_obj.mobile, 'cer': doc.certificate, 'res': doc.resume, 'photo': doc.photo}]

        return JsonResponse({'updata': emp_obj1})

    except Exception as e:
        print(e)


def getattendance(request):
    attendance = workinghours.objects.all()
    attendance_obj = [{'id': i.id, 'empid': i.employeeid, 'empname': i.employeename, 'date': i.date, 'checkin': i.checkin, 'checkout': i.checkout, 'th': i.totalhours}
                      for i in attendance]
    return JsonResponse({'attendance': attendance_obj})


def delemployee(request):
    delid = request.POST['id']
    print(delid)
    employeedetail.objects.filter(id=delid).update(status=0)
    return JsonResponse({'msg': "data deleted succcessfully"})


def fnupdate(request):
    try:
        if request.method == 'POST':
            firstname = request.POST.get('firstname')
            print(firstname)
            middlename = request.POST.get('mname')
            print(middlename)
            lastname = request.POST.get('lname')
            print(lastname)
            email = request.POST.get('email')
            print(email)
            password = request.POST.get('password')
            print(password)
            day = request.POST.get('day')
            print(day)
            month = request.POST.get('month')
            print(month)
            year = request.POST.get('year')
            print(year)
            date = year+'-'+month+'-'+day
            print(date)
            gender = request.POST.get('gender')
            print(gender)
            fathersname = request.POST.get('fathersname')
            print(fathersname)
            marital = request.POST.get('marital')
            print(marital)
            personalemail = request.POST.get('pemail')
            print(personalemail)
            address = request.POST.get('address')
            print(address)
            city = request.POST.get('city')
            print(city)
            country = request.POST.get('country')
            print(country)
            pincode = request.POST.get('pincode')
            print(pincode)
            mobile = request.POST.get('mobile')
            print(mobile)
            empid = request.POST.get('empid')
            print(empid)
            employeetype = request.POST.get('emptype')
            print(employeetype)
            department_id = request.POST.get('department')
            print(department_id)
            designation_id = request.POST.get('designation')
            print(designation_id)
            days = request.POST.get('days')
            print(days)
            months = request.POST.get('months')
            print(months)
            years = request.POST.get('years')
            print(years)
            dates = years+'-'+months+'-'+days
            print(dates)
            employeegrade = request.POST.get('empgrade')
            print(employeegrade)
            shift = request.POST.get('shift')
            print(shift)
            certificate = request.FILES.get('certificate')
            certificate_name = str(random())+certificate.name
            print(certificate_name)
            certificate_obj = FileSystemStorage()
            certificate_obj.save(certificate_name, certificate)
            resume = request.FILES.get('resume')
            resume_name = str(random())+resume.name
            print(resume_name)
            resume_obj = FileSystemStorage()
            resume_obj.save(resume_name, resume)
            photo = request.FILES.get('photo')
            photo_name = str(random())+photo.name
            print(photo_name)
            photo_obj = FileSystemStorage()
            photo_obj.save(photo_name, photo)
            employeedetail.objects.filter(id=empid).update(firstname=firstname, middlename=middlename, lastname=lastname,
                                                           date=date, gender=gender, fathersname=fathersname, maritalstatus=marital, email=email, employeetype=employeetype, department_id_id=department_id, designation_id_id=designation_id,
                                                           doj=dates, employeegrade=employeegrade, shift=shift,)
            login.objects.filter(user_id_id=empid).update(
                username=email, password=password)
            document.objects.filter(personal_id_id=empid).update(
                certificate=certificate_name, resume=resume_name, photo=photo_name)
            contactdetails.objects.filter(personal_id_id=empid).update(personalemail=personalemail, address=address, city=city,
                                                                       country=country, pincode=pincode, mobile=mobile)
            return JsonResponse({'msg': 'Data updated successfully'})
    except Exception as e:
        print(e)
    return render(request, 'employeess.html')


def manageleave(request):
    return render(request, 'manageleave.html')


def createleave(request):
    try:
        if request.method == 'POST':
            empname = request.POST['empname']
            print(empname)
            empid = request.POST['empid']
            print(empid)
            lcategory = request.POST['lcategory']
            print(lcategory)
            startdate = request.POST['startdate']
            print(startdate)
            enddate = request.POST['enddate']
            print(enddate)
            lreason = request.POST['lreason']
            print(lreason)
            remark = request.POST['remark']
            print(remark)
            status = 1
            cleave_obj = leave(employeename=empname, leavecategory_id=lcategory, startdate=startdate,
                               enddate=enddate, reason=lreason, remark=remark, employeeid_id=empid, status=status)
            cleave_obj.save()
            print(cleave_obj)

            return render(request, 'createleave', {'msg': "Data inserted successfully"})
    except Exception as e:
        print(e)
    leave_obj = leavetype.objects.all()
    return render(request, 'createleave.html', {'leave': leave_obj})


def fnmanageleave(request):
    mleave = leave.objects.all().select_related(
        'leavecategory')

    mleave_obj = [{'id': i.id, 'empname': i.employeename, 'empid': i.employeeid_id, 'lcat': i.leavecategory.leavetype,
                   'sd': i.startdate, 'ed': i.enddate, 'reason': i.reason, 'remark': i.remark, 'status': i.status}for i in mleave]
    print(mleave_obj)
    return JsonResponse({'mleave': mleave_obj})


def searchleave(request):
    search = request.POST['search']
    print(search)
    mleave = leave.objects.filter(Q(employeename=search) | Q(employeeid=search)).select_related(
        'leavecategory')
    s_obj = [{'id': i.id, 'empname': i.employeename, 'empid': i.employeeid_id, 'lcat': i.leavecategory.leavetype,
              'sd': i.startdate, 'ed': i.enddate, 'reason': i.reason, 'remark': i.remark, 'status': i.status}for i in mleave]
    return JsonResponse({'mleave': s_obj})


def getleave(request):
    try:
        if request.method == 'POST':
            lid = request.POST['uid']
            leav = leave.objects.get(id=lid)
            leave_obj = [{'id': leav.id, 'empid': leav.employeeid_id, 'empname': leav.employeename, 'ltype': leav.leavecategory_id,
                          'sd': leav.startdate, 'ed': leav.enddate, 'reason': leav.reason}]
            return JsonResponse({'leave': leave_obj})
    except Exception as e:
        print(e)


def attendance(request):
    return render(request, 'attendancelist.html')


def fnresignation(request):
    return render(request, 'resignation.html')


def createresignation(request):
    # try:
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
        status = 1
        resignation_obj = resignation(employeename=empname,
                                      resignationdate=resdate, noticeperiod=np, description=desc, employeeid_id=empid, status=status)
        resignation_obj.save()
        print(resignation_obj)

        return render(request, 'createresignation.html', {'msg': "Data inserted"})
    # except Exception as e:
    #     print(e)
    return render(request, 'createresignation.html')


def fnresignations(request):
    resign = resignation.objects.all()
    resign_obj = [{'id': i.id, 'empid': i.employeeid_id, 'employeename': i.employeename, 'resignationdate': i.resignationdate, 'noticeperiod': i.noticeperiod,
                   'description': i.description, 'status': i.status}for i in resign]
    print(resign_obj)
    return JsonResponse({'resign': resign_obj})


def getresignation(request):
    try:
        if request.method == 'POST':
            resid = request.POST['uid']
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


def delresignation(request):
    delid = request.POST['id']
    print(delid)
    resignation.objects.filter(id=delid).update(status=0)
    return JsonResponse({'msg': "data deleted succcessfully"})


def meetings(request):
    meetings_obj = meeting.objects.all()
    return render(request, 'meetings.html', {'meetings': meetings_obj})


def addmeetings(request):
    try:
        if request.method == 'POST':
            mtitle = request.POST['meetingtitle']
            print(mtitle)
            mdate = request.POST['meetingdate']
            print(mdate)
            mtime = request.POST['meetingtime']
            print(mtime)
            agenda = request.POST['agenda']
            print(agenda)
            status = 1
            addmeetings_obj = meeting(
                mtitle=mtitle, mdate=mdate, mtime=mtime, agenda=agenda, status=status)
            addmeetings_obj.save()
            print(addmeetings_obj)
            return render(request, 'addmeetings.html', {'msg': 'Meeting added succesfully'})
    except Exception as e:
        print(e)
    return render(request, 'addmeetings.html')


def fnmeeting(request):
    meet = meeting.objects.filter(status=1)
    meet_obj = [{'id': i.id, 'mtitle': i.mtitle, 'mdate': i.mdate,
                 'mtime': i.mtime, 'agenda': i.agenda}for i in meet]
    return JsonResponse({'meet': meet_obj})


def getmeeting(request):
    try:
        if request.method == 'POST':
            mid = request.POST['uid']
            meet = meeting.objects.get(id=mid)
            meet_obj = [{'id': meet.id, 'mtitle': meet.mtitle,
                         'mdate': meet.mdate, 'mtime': meet.mtime, 'agenda': meet.agenda}]
            return JsonResponse({'meet': meet_obj})
    except Exception as e:
        print(e)


def updatemeet(request):
    try:
        if request.method == 'POST':
            id = request.POST['id']
            mtitle = request.POST['mtitle']
            mdate = request.POST['mdate']
            mtime = request.POST['mtime']
            agenda = request.POST['agenda']
            meeting.objects.filter(id=id).update(
                mtitle=mtitle, mdate=mdate, mtime=mtime, agenda=agenda)
            return JsonResponse({'msg': "Data updated successfully"})
    except Exception as e:
        print(e)


def delmeeting(request):
    delid = request.POST['id']
    print(delid)
    meeting.objects.filter(id=delid).update(status=0)
    return JsonResponse({'msg': "data deleted succcessfully"})


def fnleave(request):
    try:
        leave = request.POST['leavetype']
        status = 1
        leave_obj = leavetype.objects.filter(leavetype=leave).exists()
        if leave_obj == False:

            leave_obje = leavetype(leavetype=leave, status=status)
            leave_obje.save()
            print(leave_obje)
            return render(request, 'leavetype.html', {'msg': 'Leavetype added successfully'})
        else:
            return render(request, 'leavetype.html', {'message': 'Leavetype already exist'})
    except Exception as e:
        print(e)
    return render(request, 'leavetype.html')


def fnleavetype(request):
    leave_type = leavetype.objects.filter(status=1)
    print(leave_type)
    leave = [{'id': i.id, 'leavetype': i.leavetype} for i in leave_type]
    print(leave)
    return JsonResponse({'leave': leave})


def delleavetype(request):
    delid = request.POST['id']
    print(delid)
    leavetype.objects.filter(id=delid).update(status=0)
    return JsonResponse({'msg': "data deleted succcessfully"})


def notifications(request):
    notify = notification.objects.all()
    return render(request, 'notifications.html', {'notify': notify})


def createnotifications(request):
    try:
        if request.method == 'POST':
            notify = request.POST['notify']
            print(notify)
            notify_obj = notification(notify=notify)
            notify_obj.save()
            return render(request, 'addnotifications.html', {'msg': 'Notification added successfully'})
    except Exception as e:
        print(e)
    return render(request, 'addnotifications.html')


def getnotification(request):
    notify = notification.objects.all()
    notify_obj = [{'notify': i.notify} for i in notify]
    return JsonResponse({'notify': notify_obj})


def fnpromotion(request):
    return render(request, 'promotion.html')


def createpromotion(request):
    try:
        if request.method == 'POST':
            empid = request.POST['employeeid']
            print(empid)
            empfname = request.POST['employeefname']
            print(empfname)
            emplname = request.POST['employeelname']
            print(emplname)
            designation = request.POST['designation']
            print(designation)
            ptitle = request.POST['promotiontitle']
            print(ptitle)
            pdate = request.POST['promotiondate']
            print(pdate)
            remarks = request.POST['remarks']
            print(remarks)
            status = 1
            promotion_obj = promotion(employeeid_id=empid, firstname=empfname, lastname=emplname,
                                      designation=designation, promotiontitle=ptitle, promotiondate=pdate, remarks=remarks, status=status)
            promotion_obj.save()
            print(promotion_obj)
            return render(request, 'createpromotion.html', {'msg': "Data inserted successfully"})
    except Exception as e:
        print(e)
    return render(request, 'createpromotion.html')


def fnpromotions(request):
    promo = promotion.objects.filter(status=1)
    promo_obj = [{'id': i.id, 'empid': i.employeeid_id, 'firstname': i.firstname, 'lastname': i.lastname, 'designation': i.designation,
                  'ptitle': i.promotiontitle, 'pdate': i.promotiondate, 'remarks': i.remarks}for i in promo]
    print(promo_obj)
    return JsonResponse({'promo': promo_obj})


def getpromotion(request):
    try:
        if request.method == 'POST':
            empid = request.POST['uid']
            print(empid)
            promot = promotion.objects.get(id=empid)
            promo_obj = [{'id': promot.id, 'empid': promot.employeeid_id, 'fname': promot.firstname, 'designation': promot.designation,
                          'ptitle': promot.promotiontitle, 'pdate': promot.promotiondate, 'remark': promot.remarks}]
            print(promo_obj)
            return JsonResponse({'promot': promo_obj})
    except Exception as e:
        print(e)


def updatepromotion(request):
    try:
        if request.method == 'POST':
            id = request.POST['id']
            print(id)
            empid = request.POST['empid']
            print(empid)
            empfname = request.POST['empname']
            print(empfname)

            designation = request.POST['designation']
            print(designation)
            ptitle = request.POST['ptitle']
            print(ptitle)
            pdate = request.POST['pdate']
            print(pdate)
            remarks = request.POST['remark']
            print(remarks)

            promotion.objects.filter(id=id).update(employeeid_id=empid, firstname=empfname,
                                                   designation=designation, promotiontitle=ptitle, promotiondate=pdate, remarks=remarks)
            return JsonResponse({'msg': 'Data updated successfully'})
    except Exception as e:
        print(e)


def delpromotion(request):
    delid = request.POST['id']
    print(delid)
    promotion.objects.filter(id=delid).update(status=0)
    return JsonResponse({'msg': "data deleted succcessfully"})


def complaints(request):

    return render(request, 'complaints.html')


def addcomplaints(request):
    try:
        if request.method == 'POST':
            c_f = request.POST['cf']
            print(c_f)
            c_a = request.POST['ca']
            print(c_a)
            titles = request.POST['title']
            print(titles)
            day = request.POST['day']
            print(day)
            month = request.POST['month']
            print(month)
            year = request.POST['year']
            print(year)
            date = year+'-'+month+'-'+day
            print(date)
            descriptions = request.POST['description']
            status = 1
            ac_obj = complaint(cf=c_f, ca=c_a, title=titles,
                               doc=date, description=descriptions, status=status)
            ac_obj.save()
            print(ac_obj)
            return render(request, 'addcomplaints.html', {'msg': 'complaint added successfully'})
    except Exception as e:
        print(e)
    return render(request, 'addcomplaints.html')


def fncomplain(request):
    complain = complaint.objects.filter(status=1)
    complain_obj = [{'id': i.id, 'cf': i.cf, 'ca': i.ca,
                     'title': i.title, 'date': i.doc, 'desc': i.description} for i in complain]
    return JsonResponse({'complain': complain_obj})


def getcomplain(request):
    try:
        if request.method == 'POST':
            cid = request.POST['uid']
            complain = complaint.objects.get(id=cid)
            complain_obj = [{'id': complain.id, 'cf': complain.cf, 'ca': complain.ca,
                             'title': complain.title, 'date': complain.doc, 'desc': complain.description}]
            return JsonResponse({'complain': complain_obj})
    except Exception as e:
        print(e)


def updatecomplain(request):
    try:
        if request.method == 'POST':
            id = request.POST['id']
            print(id)
            c_f = request.POST['cf']
            print(c_f)
            c_a = request.POST['ca']
            print(c_a)
            titles = request.POST['title']
            print(titles)
            descriptions = request.POST['desc']
            print(descriptions)
            complaint.objects.filter(id=id).update(cf=c_f, ca=c_a, title=titles,
                                                   description=descriptions)
            return JsonResponse({'msg': 'Data updated successfully'})
    except Exception as e:
        print(e)


def holidays(request):
    try:
        if request.method == 'POST':
            day = request.POST['day']
            print(day)
            date = request.POST['date']
            print(date)
            occassion = request.POST['occassion']
            print(occassion)
            type = request.POST['type']
            print(type)
            status = 1
            holiday_obj = holiday(day=day, date=date,
                                  occassion=occassion, holidaytype=type, status=status)
            holiday_obj.save()
            return render(request, 'holidays.html', {'msg': 'Data updated'})
    except Exception as e:
        print(e)
    return render(request, 'holidays.html')


def fnholidays(request):
    holidays = holiday.objects.filter(status=1)
    holiday_obj = [{'id': i.id, 'day': i.day, 'date': i.date,
                    'occassion': i.occassion, 'type': i.holidaytype} for i in holidays]
    print(holiday_obj)
    return JsonResponse({'holiday': holiday_obj})


def dashboards(request):
    arr = []
    dept = employeedetail.objects.all().select_related('department_id')
    for i in dept:
        arr.append([i.department_id.department_name, i.id])
    print(arr)
    return render(request, 'dashboards.html', {'item': arr})


def getdatas(request):
    user = employeedetail.objects.all()
    user_obj = [{'id': i.id} for i in user]
    holidays = holiday.objects.all().count()
    return JsonResponse({'user': user_obj, 'holiday': holidays})


def designations(request):
    try:
        desig = request.POST['designations']
        status = 1
        desig_obj = designation.objects.filter(designation_name=desig).exists()
        if desig_obj == False:
            dept = request.POST['dept']
            print(dept)
            des_obj = designation(designation_name=desig,
                                  department_id_id=dept, status=status)
            des_obj.save()
            # print(des_obj)
            return render(request, 'designation.html', {'msg': 'Designation added successfully'})
        else:
            return render(request, 'designation.html', {'message': 'Designation already exist'})
    except Exception as e:
        print(e)
    department_obj = department.objects.all()
    designation_obj = designation.objects.all()
    # print(department_obj)
    return render(request, 'designation.html', {'departments': department_obj, 'designations': designation_obj})


def fndesignation(request):
    desig = designation.objects.filter(
        status=1).select_related('department_id')
    desig_obj = [{'id': i.id, 'dname': i.department_id.department_name,
                  'desname': i.designation_name} for i in desig]
    return JsonResponse({'designation': desig_obj})


def deldesignation(request):
    delid = request.POST['id']
    print(delid)
    designation.objects.filter(id=delid).update(status=0)
    return JsonResponse({'msg': "data deleted succcessfully"})


def departments(request):
    try:
        depart = request.POST['departments']
        status = 1
        dept_obj = department.objects.filter(department_name=depart).exists()
        if dept_obj == False:
            dep_obj = department(department_name=depart, status=status)
            dep_obj.save()
            print(dep_obj)
            # return JsonResponse({'msg': 'Data inserted successfully'})
            return render(request, 'department.html', {'msg': 'Department added successfully'})
        else:
            # return JsonResponse({'msg': 'Data already exist'})
            return render(request, 'department.html', {'message': 'Department already exist'})
    except Exception as e:
        print(e)
    department_obj = department.objects.all()

    return render(request, 'department.html', {'departments': department_obj})


def fndepartment(request):
    depart = department.objects.filter(status=1)
    depart_obj = [{'id': i.id, 'dname': i.department_name} for i in depart]
    return JsonResponse({'department': depart_obj})


def deldepartment(request):
    delid = request.POST['id']
    print(delid)
    department.objects.filter(id=delid).update(status=0)
    return JsonResponse({'msg': "data deleted succcessfully"})


def fnpayroll(request):
    dept = department.objects.all()
    return render(request, 'payroll.html', {'dept': dept})


def getemployee(request):
    try:
        if request.method == 'POST':
            dept = request.POST['dept']
            print(dept)
            emf_obj = employeedetail.objects.filter(department_id_id=dept)
            emf = [{'emp_name': i.firstname, 'id': i.id}
                   for i in emf_obj]
            print(emf)
            return JsonResponse({'emf': emf})
    except Exception as e:
        print(e)


def getlastname(request):
    try:
        if request.method == 'POST':
            elm = request.POST['efm']
            print(elm)
            elm_obj = employeedetail.objects.filter(firstname=elm)
            elm = [{'elm_name': i.lastname, 'id': i.id}
                   for i in elm_obj]
            print(elm)
            return JsonResponse({'elm': elm})
    except Exception as e:
        print(e)


def getsalary(request):
    try:
        if request.method == 'POST':
            efm = request.POST['efm']
            print(efm)
            elm = request.POST['elm']
            print(elm)
            salary_obj = employeedetail.objects.filter(
                firstname=efm, lastname=elm)
            print(salary_obj)
            salary = [{'salary': i.salary} for i in salary_obj]
            print(salary)
            return JsonResponse({'salary': salary})
    except Exception as e:
        print(e)


def fnallowance(request):
    try:
        atype = request.POST['atype']
        print(atype)
        allowance_obj = allowance.objects.filter(allowancetype=atype).exists()
        if allowance_obj == False:
            amount = request.POST['amount']
            print(amount)
            a_obj = allowance(allowancetype=atype, amount=amount)
            a_obj.save()
            return render(request, 'allowance.html', {'msg': 'Data inserted'})
    except Exception as e:
        print(e)
    return render(request, 'allowance.html')


def getallowance(request):
    a_obj = allowance.objects.all()
    allow = [{'id': i.id, 'atype': i.allowancetype, 'amount': i.amount}
             for i in a_obj]
    return JsonResponse({'allowance': allow})


def allowancedata(request):
    a_obj = allowance.objects.all()
    allow = [{'amount': i.amount}
             for i in a_obj]
    return JsonResponse({'allowance': allow})


def calculate(request):
    try:
        if request.method == 'POST':
            sa = int(request.POST['sa'])
            print(sa)
            ma = int(request.POST['ma'])
            print(ma)
            conveyance = int(request.POST['conveyance'])
            print(conveyance)
            ptax = 150
            allowance = int(sa+ma+conveyance)
            print(allowance)
            sal = int(request.POST['salary'])
            print(sal)
            salary = round(sal/12, 0)
            tds = int(request.POST['tds'])
            print(tds)
            salar = salary-allowance
            print(salar)
            basic = round(salar*0.6, 0)
            print(basic)
            hra = round(salar*0.4, 0)
            print(hra)
            gearnings = basic+hra+allowance
            print(gearnings)
            gdeduction = ptax+tds
            print(gdeduction)
            netpay = gearnings-gdeduction
            print(netpay)
            payroll_obj = payroll(salary=sal, basic=basic, hra=hra, specialallowance=sa, medicalallowance=ma, conveyance=conveyance,
                                  grossearning=gearnings, ptax=ptax, tds=tds, grossdeduction=gdeduction, netpay=netpay)

            payroll_obj.save()
            print(payroll_obj)
            pay = payroll.objects.filter(salary=sal, tds=tds)
            pay_obj = [{'basic': i.basic, 'hra': i.hra, 'sa': i.specialallowance, 'ma': i.medicalallowance, 'conveyance': i.conveyance,
                        'gearning': i.grossearning, 'ptax': i.ptax, 'tds': i.tds, 'gdeduction': i.grossdeduction, 'netpay': i.netpay} for i in pay]
            print(pay_obj)
            return JsonResponse({'pay': pay_obj})
    except Exception as e:
        print(e)
    return render(request, 'payroll.html')


def setting(request):
    try:
        cpass = request.session['log']
        print(cpass)
        cpass_obj = adminlogin.objects.get(id=cpass)
        opassword = request.POST['opassword']
        print(opassword)
        npassword = request.POST['newpassword']
        if cpass_obj.password == opassword:
            cpass_obj.password = npassword
            cpass_obj.save()
            return render(request, 'setting.html', {'msg': 'password changed successfully'})
    except Exception as e:
        print(e)
    return render(request, 'setting.html')


def approveleave(request):
    try:
        id = request.session['log']
        print(id)
        user = employeedetail.objects.get(id=id)
        print(user)
        leave.objects.filter(employeeid_id=id).update(status='Approved')
        subject = 'Leave approval'
        message = f'Hi {user.firstname}, your leave has been approved'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [user.email, ]
        print(recipient_list)
        send_mail(subject, message, email_from, recipient_list)
        return JsonResponse({'msg': 'Msg send'})
    except Exception as e:
        print(e)


def rejectleave(request):
    try:
        id = request.session['log']
        print(id)
        user = employeedetail.objects.get(id=id)
        print(user)
        leave.objects.filter(employeeid_id=id).update(status='Reject')
        subject = 'Leave approval'
        message = f'Hi {user.firstname}, your leave has been rejected'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [user.email, ]
        print(recipient_list)
        send_mail(subject, message, email_from, recipient_list)
        return JsonResponse({'msg': 'Msg send'})
    except Exception as e:
        print(e)


def approveresignation(request):
    try:
        id = request.session['log']
        print(id)
        user = employeedetail.objects.get(id=id)
        print(user)
        resignation.objects.filter(employeeid_id=id).update(status='Approved')
        subject = 'Resignation Approval'
        message = f'Hi {user.firstname}, your resignation has been approved'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [user.email, ]
        print(recipient_list)
        send_mail(subject, message, email_from, recipient_list)
        return JsonResponse({'msg': 'Msg send'})
    except Exception as e:
        print(e)


def rejectresignation(request):
    try:
        id = request.session['log']
        print(id)
        user = employeedetail.objects.get(id=id)
        print(user)
        resignation.objects.filter(employeeid_id=id).update(status='Reject')
        subject = 'Resignation Approval'
        message = f'Hi {user.firstname}, your resignation has been rejected'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [user.email, ]
        print(recipient_list)
        send_mail(subject, message, email_from, recipient_list)
        return JsonResponse({'msg': 'Msg send'})
    except Exception as e:
        print(e)


def getpresent(request):
    try:
        if request.method == 'POST':
            id = request.session['log']
            date = request.POST['date']
            print(date)
            present = workinghours.objects.filter(
                employeeid=id, date=date).count()
            print(present)
            return JsonResponse({'present': present})
    except Exception as e:
        print(e)


def loadchart(request):
    # result = (employeedetail.objects
    #           .values('department_id')
    #           .annotate(count=Count('department_id'))
    #           .order_by()
    #           )
    # for i in result:
    #     print(i)

    result = employeedetail.objects.select_related('department_id')
    res = [{'departname': i.department_id.department_name} for i in result]

    return JsonResponse({'key': res})
