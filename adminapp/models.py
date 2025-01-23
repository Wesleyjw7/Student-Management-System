from django.db import models

class Admin(models.Model):
    id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=100,blank=False,unique=True)
    password=models.CharField(max_length=100,blank=False)

    class Meta:
        db_table="admin_table"

    def __str__(self):
        return self.username

class Course(models.Model):
    id = models.AutoField(primary_key=True)
    department_choices = (("CSE(Regular)", "CSE(R)"), ("CSE(HONORS)", "CSE(H)"), ("CSE(IT)", "CSIT"),("ECE","ECE"))
    department = models.CharField(max_length=100, blank=False,choices=department_choices)
    ac_year_choice=(("2024-2025","2024-2025"),("2023-2024","2023-2024"),("2022-2023","2022-2023"))
    academicyear = models.CharField(max_length=20, blank=False,choices=ac_year_choice)
    sem_choices=(("Even","Even"),("Odd","Odd"))
    semester = models.CharField(max_length=10, blank=False)
    year = models.IntegerField(blank=False)
    coursecode=models.CharField(max_length=20,blank=False)
    coursetitle=models.CharField(max_length=100,blank=False)
    credits=models.FloatField(blank=False)


    class Meta:
        db_table="course_table"

    def __str__(self):
        return self.coursetitle

class Student(models.Model):
    id = models.AutoField(primary_key=True)
    studentid=models.BigIntegerField(blank=False,unique=True)
    fullname=models.CharField(max_length=100,blank=False)
    gender_choices=(("Male","Male"),("Female","Female"),("Others","Others"))
    gender=models.CharField(max_length=20,blank=False,choices=gender_choices)
    program_choices=(("B.Tech.","B.Tech."),("M.Tech.","M.Tech."))
    program = models.CharField(max_length=50, blank=False,choices=program_choices)
    department_choices = (("CSE(Regular)", "CSE(R)"), ("CSE(HONORS)", "CSE(H)"), ("CSE(IT)", "CSIT"), ("ECE", "ECE"))
    department=models.CharField(max_length=50,blank=False,choices=department_choices)
    sem_choices = (("Even", "Even"), ("Odd", "Odd"))
    semester=models.CharField(max_length=10,blank=False,choices=sem_choices)
    year=models.IntegerField(blank=False)
    email = models.CharField(max_length=100, blank=False, unique=True)
    password = models.CharField(max_length=100, blank=False,default="RCEE")
    contact=models.CharField(max_length=20,blank=False,unique=True)

    class Meta:
        db_table="student_table"

    def __str__(self):
        return self.fullname

class Faculty(models.Model):
    id = models.AutoField(primary_key=True)
    facultyid = models.BigIntegerField(blank=False, unique=True)
    fullname = models.CharField(max_length=100, blank=False)
    gender_choices=(("Male","Male"),("Female","Female"),("Others","Others"))
    gender = models.CharField(max_length=20, blank=False,choices=gender_choices)
    designation_Choices=(("M.Tech.","M.Tech."),("Ph.D.","Ph.D."))
    designation = models.CharField(max_length=50, blank=False,choices=designation_Choices)
    department_choices = (("CSE(Regular)", "CSE(R)"), ("CSE(HONORS)", "CSE(H)"), ("CSE(IT)", "CSIT"), ("ECE", "ECE"))
    department = models.CharField(max_length=50, blank=False,choices=department_choices)
    qualification_choices=(("Prof.","Professor"),("Assoc. Prof","Associate Professor"),("Asst. Prof","Assistant Professor"))
    qualification = models.CharField(max_length=30, blank=False,choices=qualification_choices)
    email = models.CharField(max_length=100, blank=False, unique=True)
    password = models.CharField(max_length=100, blank=False, default="RCEE")
    contact = models.CharField(max_length=20, blank=False, unique=True)

    class Meta:
        db_table = "faculty_table"

    def __str__(self):
        return self.fullname


class Facultycoursemapping(models.Model):
    mapping_id = models.AutoField(primary_key=True)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)

    component_choices=(("Lecture","Lecture"),("Tutorial","Tutorial"),("Practical","Practical"),("Skilling","Skilling"))
    component=models.CharField(max_length=10,blank=False,choices=component_choices,default="L")

    type = models.BooleanField(blank=False,default=True)
    section = models.IntegerField(blank=False,default=1)


    class Meta:
        db_table="facultycoursemapping_table"

    def __str__(self):
        return f"{self.faculty.fullname} - {self.course.coursetitle} - {self.component}"

