from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render, redirect
from adminapp.models import Faculty
from adminapp.models import Course,Facultycoursemapping
from django.contrib.auth.hashers import check_password


def facultyhome(request):
    facultyid = request.session.get("ffid")
    if not facultyid:
        return redirect("facultylogin")
    return render(request, "facultyhome.html", {"ffid": facultyid})


def facultylogin(request):
    return render(request, "facultylogin.html")



def checkfacultylogin(request):
    facultyid = request.POST["fid"]
    facultypwd = request.POST["pwd"]

    flag = Faculty.objects.filter(Q(facultyid=facultyid) & Q(password=facultypwd))
    if flag:
        request.session["ffid"]=facultyid
        return render(request, "facultyhome.html",{"ffid":facultyid})
    else:
        messages.success(request,"Login Failed")
        return render(request, "facultylogin.html")

def facultychangepassword(request):
    facultyid = request.session["ffid"]
    return render(request,"facultychangepassword.html",{"ffid":facultyid})

def facultyupdatepwd(request):
    facultyid = request.session["ffid"]
    facultyopwd = request.POST["fopwd"]
    facultynpwd = request.POST["fnpwd"]
    facultycpwd = request.POST["fcpwd"]
    if facultynpwd==facultycpwd:
        flag=Faculty.objects.filter(Q(facultyid=facultyid)&Q(password=facultyopwd))
        if flag:
            Faculty.objects.filter(facultyid=facultyid).update(password=facultynpwd)
            messages.success(request, "Updated successfully!")
            return redirect("facultychangepassword")
        else:
            messages.error(request,"Incorrect Password")
            return redirect("facultychangepassword")
    else:
        messages.error(request,"New Password and Confirm Password must be Same")
        return redirect("facultychangepassword")

def facultycourses(request):
    ffid = request.session["ffid"]
    mappingcourses = Facultycoursemapping.objects.all()
    fcourse = []
    for mapping in mappingcourses:
        if mapping.faculty.facultyid == int(ffid):
            fcourse.append(mapping)
            print(mapping)
    return render(request, "facultycourses.html", {"adname":ffid,"coursedata": fcourse})


def facultylogout(request):
    request.session.flush()
    return redirect("facultylogin")