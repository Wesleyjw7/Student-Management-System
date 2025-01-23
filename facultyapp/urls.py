from django.urls import path
from . import views

urlpatterns = [
    path("facultyhome/", views.facultyhome, name="facultyhome"),
    path("facultylogin/", views.facultylogin, name="facultylogin"),
    path("facultylogin/checkfacultylogin", views.checkfacultylogin, name="checkfacultylogin"),
    path("facultychangepassword",views.facultychangepassword,name="facultychangepassword"),
    path("facultyupdatepwd",views.facultyupdatepwd,name="facultyupdatepwd"),
    path("facultycourses", views.facultycourses, name="facultycourses"),
]
