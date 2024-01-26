from django.shortcuts import render
from app.models import *
from django.http import HttpResponse

# Create your views here.
def display_emp(request):
    QLEO=Employee.objects.all()
    d={'employee':QLEO}
    return render(request,'display_emp.html',d)

def display_dept(request):
    QLDO=Department.objects.all()
    d={'department':QLDO}
    return render(request,'display_department.html',d)

def insert_emp (request):
    dn=input('enter deptno: ')
    en=input('enter ename : ')
    es=input('enter esal  : ')
    ed=input('enter edate : ')
    DO=Department.objects.get(dept_no=dn)
    EO=Employee.objects.get_or_create(dept_no=DO,ename=en,esal=es,edate=ed)[0]
    EO.save()
    return HttpResponse('employee is added')

