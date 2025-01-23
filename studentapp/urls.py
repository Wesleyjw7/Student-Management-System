from django.urls import path
from . import views

urlpatterns = [
    path("studenthome/", views.studenthome, name="studenthome"),
    path("studentlogin/", views.studentlogin, name="studentlogin"),
    path("studentlogin/checkstudentlogin", views.checkstudentlogin, name="checkstudentlogin"),
    path("studentchangepassword",views.studentchangepassword,name="studentchangepassword"),
    path("studentupdatepwd",views.studentupdatepwd,name="studentupdatepwd"),
    path("studentcourse",views.studentcourse,name="studentcourse"),
    path("studentviewcourse",views.studentviewcourse,name="studentviewcourse"),
]
