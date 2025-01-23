from django import forms
from .models import Faculty


class AddFacultyForm(forms.ModelForm):
    class Meta:
        model = Faculty
        fields = "__all__"
        exclude={"password"}


class AddFacultyForm1(forms.ModelForm):
    class Meta:
        model = Faculty
        fields = "__all__"
        exclude={"password","facultyid","gender","fullname"}