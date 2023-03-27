from django.db import models

# Create your models here.
Gender = (('Male','Male'),('Female','Female'),('Other','Other'))
class Employee(models.Model):
    Employee_Id = models.IntegerField(primary_key=True)
    Employee_Name=models.TextField(max_length=200)
    Employee_Email=models.EmailField(max_length=254,default="")
    Employee_Age= models.IntegerField()
    Employee_Sex=models.CharField(max_length=200,choices  = Gender)
    Employee_JDate= models.DateField(auto_now_add=True)
    Employee_Salary=models.DecimalField(max_digits=1000000, decimal_places = 2)
    def __str__(self):
        return self.Employee_Email
class Project(models.Model):
    Project_Name=models.CharField(max_length=500)
    Project_Start_Date = models.DateField(auto_now_add=True)
    Project_End_Date=models.DateField()
    def __str__(self):
        return self.Project_Name
class Department (models.Model):
    Department_Id = models.IntegerField(primary_key=True)
    Department_Name = models.CharField(max_length=200)
    Department_Emp = models.ForeignKey(Employee, on_delete=models.CASCADE)
    Department_project = models.ForeignKey(Project, on_delete=models.CASCADE) 
    def __str__(self):
        return self.Department_Name   
class Company(models.Model):
    CEO = models.CharField(max_length=500)
    Name =models.CharField(max_length=500)
    department=models.ForeignKey(Department, on_delete=models.CASCADE)
    project=models.ForeignKey(Project,on_delete=models.CASCADE)
    def __str__(self):
        return self.Name
  
    
