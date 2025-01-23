from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns=[
    path("adminhome",views.adminhome,name="adminhome"),
    path("logout",views.logout,name="logout"),
    path("login/checkadminlogin", views.checkadminlogin, name="checkadminlogin"),


    path("viewstudent",views.viewstudent,name="viewstudent"),
    path("adminstudent",views.adminstudent,name="adminstudent"),
    path("addstudent",views.addstudent,name="addstudent"),
    path("insertstudent",views.insertstudent,name="insertstudent"),
    path("deletestudent",views.deletestudent,name="deletestudent"),
    path("studentdeletion/<int:sid>",views.studentdeletion,name="studentdeletion"),

    path("viewfaculty",views.viewfaculty,name="viewfaculty"),
    path("adminfaculty",views.adminfaculty,name="adminfaculty"),
    path("addfaculty",views.addfaculty,name="addfaculty"),
    path("insertfaculty", views.insertfaculty, name="insertfaculty"),
    path("deletefaculty",views.deletefaculty,name="deletefaculty"),
    path("facultydeletion/<int:fid>",views.facultydeletion,name="facultydeletion"),
    path("updatefaculty",views.updatefaculty,name="updatefaculty"),
    path("facultyupdation/<int:fid>",views.facultyupdation,name="facultyupdation"),
    path("addfaculty2",views.addfaculty2,name="addfaculty2"),
    path("Fac_cou_map",views.Fac_cou_map,name="Fac_cou_map"),


    path("viewcourse",views.viewcourse,name="viewcourse"),
    path("admincourse",views.admincourse,name="admincourse"),
    path("addcourse",views.addcourse,name="addcourse"),
    path("insertcourse", views.insertcourse, name="insertcourse"),
    path('addcourse/', views.insertcourse, name='add_course'),
    path("deletecourse",views.deletecourse,name="deletecourse"),
    path("coursedeletion/<int:cid>",views.coursedeletion,name="coursedeletion"),
    path("updatecourse",views.updatecourse,name="updatecourse"),
    path("courseupdation/<int:cid>",views.courseupdation,name="courseupdation"),
    path("course_updated/<int:cid>", views.course_updated, name="course_updated"),

    path("change_password",views.admin_change_password,name="change_password"),
    path("adminupdatepwd",views.adminupdatepwd,name="adminupdatepwd"),

]