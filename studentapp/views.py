from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render, redirect
from adminapp.models import Student, Course
from django.contrib.auth.hashers import check_password


def studenthome(request):
    studentid = request.session.get("ssid")
    student=Student.objects.get(studentid=studentid)
    if not studentid:
        return redirect("studentlogin")
    return render(request, "studenthome.html", {"ssid": studentid,"student":student})


def studentlogin(request):
    return render(request, "studentlogin.html")


def checkstudentlogin1(request):
    studentid = request.POST.get("sid")
    studentpwd = request.POST.get("pwd")

    if not studentid or not studentpwd:
        messages.error(request, "Both fields are required!")
        return render(request, "studentlogin.html")

    student = Student.objects.filter(studentid=studentid).first()
    if student and check_password(studentpwd, student.password):
        request.session["ssid"] = studentid
        return redirect("studenthome")
    else:
        messages.error(request,{studentpwd})
        return redirect("studentlogin")


def checkstudentlogin(request):
    studentid = request.POST["sid"]
    studentpwd = request.POST["pwd"]

    flag = Student.objects.filter(Q(studentid=studentid) & Q(password=studentpwd))
    if flag:
        request.session["ssid"]=studentid
        return render(request, "studenthome.html",{"ssid":studentid})
    else:
        messages.success(request,"Login Failed")
        return render(request, "studentlogin.html")


def studentchangepassword(request):
    studentid = request.session["ssid"]
    return render(request,"studentchangepassword.html",{"ssid":studentid})

def studentupdatepwd(request):
    studentid = request.session["ssid"]
    studentopwd = request.POST["opwd"]
    studentnpwd = request.POST["npwd"]
    studentcpwd = request.POST["cpwd"]
    if studentnpwd==studentcpwd:
        flag=Student.objects.filter(Q(studentid=studentid)&Q(password=studentopwd))
        if flag:
            Student.objects.filter(studentid=studentid).update(password=studentnpwd)
            messages.success(request, "Updated successfully!")
            return redirect("studentchangepassword")
        else:
            messages.error(request,"Incorrect Password")
            return redirect("studentchangepassword")
    else:
        messages.error(request,"New Password and Confirm Password must be Same")
        return redirect("studentchangepassword")


def studentcourse(request):
    studentid = request.session["ssid"]
    return render(request,"studentcourse.html",{"ssid":studentid})

def studentviewcourse(request):
    studentid = request.session["ssid"]

    year=request.POST["sy"]
    sem=request.POST["ssm"]

    courses=Course.objects.filter(Q(academicyear=year)&Q(semester=sem))
    print(courses)
    return render(request,"displaystudentcourse.html",{"ssid":studentid,"courses":courses})

def studentlogout(request):
    request.session.flush()
    return redirect("studentlogin")