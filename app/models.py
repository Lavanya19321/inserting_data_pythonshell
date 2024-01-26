from django.db import models

# Create your models here.
class Department(models.Model):
    dept_no=models.PositiveIntegerField(primary_key=True)
    dname=models.CharField(max_length=25)
    dloc=models.CharField(max_length=15)
    def __str__(self):
        return str(self.dept_no)



class Employee(models.Model):
    dept_no=models.ForeignKey(Department,on_delete=models.CASCADE)
    ename=models.CharField(max_length=25)
    esal=models.IntegerField()
    edate=models.DateField()
     
    def __str__(self):
        return self.ename

