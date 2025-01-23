from django.contrib import messages
from django.db import IntegrityError
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import AddFacultyForm,AddFacultyForm1

from .models import Admin, Student, Faculty, Course, Facultycoursemapping


def adminhome(request):
    adminuname = request.session["adname"]
    return render(request, "adminhome.html", {"adname": adminuname})



def logout(request):
    return render(request, "login.html")


def checkadminlogin(request):
    adminuname = request.POST["uname"]
    adminpwd = request.POST["pwd"]

    flag = Admin.objects.filter(Q(username=adminuname) & Q(password=adminpwd))
    if flag:
        request.session["adname"]=adminuname
        return render(request, "adminhome.html",{"adname":adminuname})
    else:
        messages.success(request,"Login Failed")
        return render(request, "login.html")


def viewstudent(request):
    students = Student.objects.all()
    return render(request, "viewstudent.html", {"studentdata": students})


def viewfaculty(request):
    facultys = Faculty.objects.all()
    return render(request, "viewfaculty.html", {"facultydata": facultys})


def viewcourse(request):
    courses = Course.objects.all()
    return render(request, "viewcourse.html", {"coursedata": courses})


def adminstudent(request):
    adminuname = request.session["adname"]
    return render(request, "adminstudent.html", {"adname": adminuname})


def adminfaculty(request):
    adminuname = request.session["adname"]
    return render(request, "adminfaculty.html", {"adname": adminuname})


def admincourse(request):
    adminuname = request.session["adname"]
    return render(request, "admincourse.html", {"adname": adminuname})


def addstudent(request):
    adminuname = request.session["adname"]
    return render(request, "addstudent.html", {"adname": adminuname})



def insertstudent(request):
    if request.method == "POST":
        sid = request.POST["sid"]
        sname = request.POST["sname"]
        sgender = request.POST["sgender"]
        sprogram = request.POST["sprogram"]
        sdept = request.POST["sdept"]
        ssem = request.POST["ssem"]
        syear = request.POST["syear"]
        semail = request.POST["semail"]
        spassword = request.POST["spassword"]
        scontact = request.POST["scontact"]

        student = Student(studentid=sid, fullname=sname, gender=sgender, program=sprogram, department=sdept,
                          semester=ssem, year=syear, email=semail, password=spassword, contact=scontact)

        try:
            student.save()
            messages.success(request, "Student added successfully!")
        except IntegrityError:
            messages.error(request, "Entered values already exist")
        return redirect('addstudent')
    else:
        return HttpResponse("invalid")


def addcourse(request):
    adminuname = request.session["adname"]
    return render(request, "addcourse.html", {"adname": adminuname})


def insertcourse(request):
    if request.method == "POST":
        cdept = request.POST["cdept"]
        cayear = request.POST["cayear"]
        courseyear = request.POST["courseyear"]
        coursesemester = request.POST["coursesemester"]
        coursecode = request.POST["coursecode"]
        coursetitle = request.POST["coursetitle"]
        course_credits=request.POST["course_credits"]

        course = Course(department=cdept, academicyear=cayear, year=courseyear, semester=coursesemester,
                        coursecode=coursecode, coursetitle=coursetitle, credits=course_credits)

        try:
            course.save()
            messages.success(request, "Student added successfully!")
        except IntegrityError:
            messages.error(request, "Entered values already exist")
        except ValueError:
            messages.error(request,"Entered wrong values")
        return redirect('addcourse')
    else:
        return render(request, 'addcourse.html')


def addfaculty(request):
    adminuname = request.session["adname"]
    return render(request, "addfaculty.html", {"adname": adminuname})


def insertfaculty(request):
    if request.method == "POST":
        fid = request.POST["fid"]
        fname = request.POST["fname"]
        fgender = request.POST["fgender"]
        fdes = request.POST["fdes"]
        fdept = request.POST["fdept"]
        fqual = request.POST["fqual"]
        femail = request.POST["femail"]
        fpassword = request.POST["fpassword"]
        fcontact = request.POST["fcontact"]

        faculty = Faculty(facultyid=fid, fullname=fname, gender=fgender, designation=fdes, department=fdept,
                          qualification=fqual, email=femail, password=fpassword, contact=fcontact)

        faculty.save()

        return HttpResponse("faculty added succesfully")
    else:
        return HttpResponse("invalid")

def deletestudent(request):
    students=Student.objects.all()
    return render(request,"deletestudent.html",{"studentdata":students})

def studentdeletion(request,sid):
    Student.objects.filter(id=sid).delete()
    return redirect("deletestudent")

def deletefaculty(request):
    facultys=Faculty.objects.all()
    return render(request,"deletefaculty.html",{"facultydata":facultys})

def facultydeletion(request,fid):
    Faculty.objects.filter(id=fid).delete()
    return redirect("deletefaculty")

def deletecourse(request):
    courses=Course.objects.all()
    return render(request,"deletecourse.html",{"coursedata":courses})

def coursedeletion(request,cid):
    Course.objects.filter(id=cid).delete()
    return redirect("deletecourse")

def updatecourse(request):
    auname=request.session["adname"]
    courses=Course.objects.all()
    return render(request,"updatecourse.html",{"adname":auname,"courses":courses})


def courseupdation(request,cid):
    return render(request,"courseupdated.html",{"cid":cid})

def course_updated(request,cid):
    coursecode=request.POST["coursecode"]
    coursetitle=request.POST["coursetitle"]
    course_credits=request.POST["course_credits"]
    if Course.objects.filter(id=cid).update(coursecode=coursecode,coursetitle=coursetitle,credits=course_credits):
        messages.success(request,"updated successfully")
        return render(request,"courseupdated.html",{"cid":cid})
    else:
        messages.error(request,"updated unsuccessfully")
        return render(request,"courseupdated.html",{"cid":cid})


def updatefaculty(request):
    auname = request.session["adname"]
    faculties=Faculty.objects.all()
    return render(request,"updatefaculty.html",{"adname":auname,"faculties":faculties})

def facultyupdation(request,fid):
    form = AddFacultyForm1()
    if request.method == "POST":
        form1 = AddFacultyForm1(request.POST)
        if form1.is_valid():
            form1.save()
            messages.success(request, "Faculty Added Successfully")
        else:
            messages.success(request, "Entered values already exist")
    adminuname = request.session["adname"]
    return render(request, "addfaculty2.html", {"form": form, "adname": adminuname})

def addfaculty2(request):
    form = AddFacultyForm()
    if request.method=="POST":
        form1=AddFacultyForm(request.POST)
        if form1.is_valid():
            form1.save()
            messages.success(request,"Faculty Added Successfully")
        else:
            messages.success(request, "Entered values already exist")
    adminuname = request.session["adname"]
    return render(request,"addfaculty2.html",{"form":form,"adname":adminuname})

def Fac_cou_map(request):
    fcourses=Facultycoursemapping.objects.all()

    adminuname = request.session["adname"]
    return render(request,"Faculty Course Mapping.html",{"uname":adminuname,"fcourses":fcourses})

def admin_change_password(request):
    adminuname = request.session["adname"]
    return render(request,"change_password.html")

def adminupdatepwd(request):
    adminuname = request.session["adname"]
    adminopwd = request.POST["aopwd"]
    adminnpwd = request.POST["anpwd"]
    admincpwd = request.POST["acpwd"]
    if adminnpwd==admincpwd:
        flag=Admin.objects.filter(Q(username=adminuname)&Q(password=adminopwd))
        if flag:
            Admin.objects.filter(username=adminuname).update(password=adminnpwd)
            messages.success(request, "Updated successfully!")
            return redirect("change_password")
        else:
            messages.error(request,"Incorrect Password")
            return redirect("change_password")
    else:
        messages.error(request,"New Password and Confirm Password must be Same")
        return redirect("change_password")





