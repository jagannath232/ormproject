from django.shortcuts import render
from django.db.models import Q
from .models import Employee
# Create your views here.


def emp_view(request):
    #emp_list = Employee.objects.all()
    #emp_list = Employee.objects.filter(ename = "Darrell Wilson")
    #emp_list = Employee.objects.filter(esal__gt = 15000)
    #emp_list = Employee.objects.filter(esal__lte = 15000)
    #emp_list = Employee.objects.filter(esal__lte = 15000)
    #emp_list = Employee.objects.filter(eno__exact = 5306)
    #emp_list = Employee.objects.filter(ename__iexact = "darrell Wilson")
    #emp_list = Employee.objects.filter(ename__contains = "Smith")
    #emp_list = Employee.objects.filter(ename__icontains = "Smith")
    #emp_list = Employee.objects.filter(id__in=(1,2,4))
    #emp_list = Employee.objects.filter(ename__startswith='J')
    #emp_list = Employee.objects.filter(ename__endswith='s')
    #emp_list = Employee.objects.filter(esal__range=(14000,17000))
    #emp_list = Employee.objects.filter(ename__startswith='D')  | Employee.objects.filter(esal__lt=15000)
    #emp_list = Employee.objects.filter(Q(ename__startswith='D')|Q(esal__lt=15000))
    #emp_list = Employee.objects.filter(ename__startswith="D") & Employee.objects.filter(esal__lt=15000)
    #emp_list = Employee.objects.filter(Q(ename__startswith="D")| Q(esal__lt=15000))
    #emp_list = Employee.objects.filter(ename__startswith="D",esal__lt=15000)
    #emp_list = Employee.objects.exclude(ename__startswith='J')
    #emp_list = Employee.objects.filter(~Q(ename__startswith='J'))
    #emp_list = Employee.objects.all().only('ename','esal','eaddr')
    #emp_list = Employee.objects.all().order_by('eno')
    #emp_list = Employee.objects.all().order_by('-eno')
    #emp_list= Employee.objects.all().order_by('-esal')[0]
    #emp_list = Employee.objects.all().order_by('ename')
    




    return render(request,'testapp/emp.html',{'emp_list':emp_list})
