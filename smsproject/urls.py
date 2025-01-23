from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    # Admin panel
    path('admin/', admin.site.urls),

    # Project-specific routes
    path("", views.demofunction, name="home"),
    path("demo/", views.demofunction1, name="demo"),
    path("demo1/", views.demofunction2, name="demo1"),
    path("SMS/", views.homefunction, name="SMS"),
    path("about/", views.aboutfunction, name="about"),
    path("login/", views.loginfunction, name="login"),
    path("contact/", views.contactfunction, name="contact"),

    # Include app-specific URL configurations with distinct prefixes
    path("", include("adminapp.urls")),
    path("", include("studentapp.urls")),
    path("", include("facultyapp.urls")),
]
