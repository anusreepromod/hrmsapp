from django.shortcuts import render
from . models import *
# Create your views here.
from random import random
from django.core.files.storage import FileSystemStorage
from django.http.response import JsonResponse


def logins(request):
    try:
        if request.method == 'POST':
            username = request.POST['username']
            print(username)
            password = request.POST['password']
            print(password)
            logi_obj = login.objects.get(username=username, password=password)
            print(logi_obj.id)
            request.session['log'] = logi_obj.id
            log_obj = employeedetail.objects.get(id=logi_obj.user_id_id)
            return render(request, 'dashboards.html', {'username': log_obj})
    except Exception as e:
        print(e)
    return render(request, 'logins.html')


def employee(request):
    users_obje = employeedetail.objects.all()
    user_obj = [{'id': i.id, 'fname': i.firstname, 'email': i.email, 'department': i.department_id_id,
                 'designation': i.designation_id_id, 'doj': i.doj}for i in users_obje]
    return JsonResponse({'user': user_obj})


def fnemployee(request):
    return render(request, 'employees.html')


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
            user_obje = employeedetail(firstname=firstname, middlename=middlename, lastname=lastname,
                                       date=date, gender=gender, fathersname=fathersname, maritalstatus=marital, email=email, employeetype=employeetype, department_id_id=department_id, designation_id_id=designation_id,
                                       doj=dates, employeegrade=employeegrade, shift=shift,)
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

    emp = request.POST['uid']
    print(emp)
    #     emp_obj = employeedetail.objects.get(id=emp)
    #     print(emp_obj)
    #     off_obj = contactdetails.object.get(personal_id_id=emp)
    #     print(off_obj)
    #     emp_obj = [{'id': emp_obj.id, 'fname': emp_obj.firstname,
    #                 'pemail': off_obj.personalemail}]

    # return JsonResponse({'data': emp_obj})
    return JsonResponse({'update': "updated"})


def manageleave(request):
    return render(request, 'manageleave.html')


def createleave(request):
    leave_obje = leavetype.objects.all()
    return render(request, 'createleave.html', {'leave': leave_obje})


def attendance(request):
    return render(request, 'attendancelist.html')


def resignation(request):
    return render(request, 'resignation.html')


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
            addmeetings_obj = meeting(
                mtitle=mtitle, mdate=mdate, mtime=mtime, agenda=agenda)
            addmeetings_obj.save()
            print(addmeetings_obj)
            return render(request, 'addmeetings.html', {'msg': 'Meeting added succesfully'})
    except Exception as e:
        print(e)
    return render(request, 'addmeetings.html')


def leave(request):
    try:
        leave = request.POST['leavetype']
        leave_obj = leavetype.objects.filter(leavetype=leave).exists()
        if leave_obj == False:
            leave_obje = leavetype(leavetype=leave)
            leave_obje.save()
            print(leave_obje)
            return render(request, 'leavetype.html', {'msg': 'Leavetype added successfully'})
        else:
            return render(request, 'leavetype.html', {'message': 'Leavetype already exist'})
    except Exception as e:
        print(e)
    leavetype_obj = leavetype.objects.all()

    return render(request, 'leavetype.html', {'leaves': leavetype_obj})


def notifications(request):
    return render(request, 'notifications.html')


def promotion(request):
    return render(request, 'promotion.html')


def complaints(request):
    complaints_obje = complaint.objects.all()
    return render(request, 'complaints.html', {'complaints': complaints_obje})


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
            ac_obj = complaint(cf=c_f, ca=c_a, title=titles,
                               doc=date, description=descriptions)
            ac_obj.save()
            print(ac_obj)
            return render(request, 'addcomplaints.html', {'msg': 'complaint added successfully'})
    except Exception as e:
        print(e)
    return render(request, 'addcomplaints.html')


def holidays(request):
    return render(request, 'holidays.html')


def dashboards(request):
    return render(request, 'dashboards.html')


def createresignation(request):
    return render(request, 'createresignation.html')


def createpromotion(request):
    return render(request, 'createpromotion.html')


def designations(request):
    try:
        desig = request.POST['designations']
        desig_obj = designation.objects.filter(designation_name=desig).exists()
        if desig_obj == False:
            dept = request.POST['dept']
            print(dept)
            des_obj = designation(designation_name=desig,
                                  department_id_id=dept)
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


def departments(request):
    try:
        depart = request.POST['departments']
        dept_obj = department.objects.filter(department_name=depart).exists()
        if dept_obj == False:
            dep_obj = department(department_name=depart)
            dep_obj.save()
            print(dep_obj)
            return JsonResponse({'msg': 'Data inserted successfully'})
            # return render(request, 'department.html', {'msg': 'Department added successfully'})
        else:
            return JsonResponse({'msg': 'Data already exist'})
            # return render(request, 'department.html', {'message': 'Department already exist'})
    except Exception as e:
        print(e)
    department_obj = department.objects.all()

    return render(request, 'department.html', {'departments': department_obj})

# def dept(request):
#     try:
#         if request.method == 'POST':
#             depart = request.POST['edepartment']
#             print(depart)
#             dep_obj = department(department_name=depart)
#             dep_obj.save()
#             print(dep_obj)
#             return render(request, 'dept.html', {'msg': 'department added successfully'})
#         else:
#             return render(request, 'dept.html')
#     except Exception as e:
#         print(e)
#     return render(request, 'dept.html')


def sample(request):
    try:
        depart = request.POST['departments']

        dept_obj = department.objects.filter(department_name=depart).exists()
        if dept_obj == False:
            dep_obj = department(department_name=depart)
            dep_obj.save()
            print(dep_obj)
            return JsonResponse({'msg': 'Data inserted successfully'})
            # return render(request, 'department.html', {'msg': 'Department added successfully'})
        else:
            return JsonResponse({'msg': 'Data already exist'})
            # return render(request, 'department.html', {'message': 'Department already exist'})
    except Exception as e:
        print(e)
    department_obj = department.objects.all()

    return render(request, 'sample.html')
