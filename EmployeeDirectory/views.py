from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Employee
from django import template
from django.contrib import messages
from rest_framework.response import Response
from rest_framework.views import APIView
from . import serializers
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

register = template.Library()


class Emp(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        emp_data = Employee.objects.all()
        serializer = serializers.EmployeeSerializer(emp_data, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = serializers.EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Create your views here.
def home(request):
    return render(request, 'EmployeeDirectory.html')


def add_emp(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        office_location = request.POST.get('office_location')
        department = request.POST.get('department')
        obj = Employee(
            name=name,
            email=email,
            office_location=office_location,
            department=department
        )
        obj.save()
        print(name, email, office_location, department)
        return HttpResponse("Employee Data Successfully added!")
    return render(request, 'add_emp.html')


def update(request, emp_id):
    print(emp_id)
    obj = Employee.objects.get(id=emp_id)
    print(obj)
    context = {
        'emp_id': obj.id,
        'name': obj.name,
        'email': obj.email,
        'office_location': obj.office_location,
        'department': obj.department
    }
    print(context)
    return render(request, 'update_emp.html', context)


def update_emp_details(request):
    if request.method == "POST":
        emp_id = request.POST.get('emp_id')
        name = request.POST.get('name')
        email = request.POST.get('email')
        office_location = request.POST.get('office_location')
        department = request.POST.get('department')
        obj = Employee.objects.get(id=emp_id)
        obj.name = name
        obj.email = email
        obj.office_location = office_location
        obj.department = department
        obj.save()
        return HttpResponse('Employee Details Updated')


def delete_emp(request, emp_id):
    try:
        record = Employee.objects.get(id=emp_id)
        record.delete()
        return HttpResponse("Employee Record Deleted")
    except:
        return HttpResponse("Record doesn't exist!")


def emp_dashboard(request):
    emp_data = Employee.objects.all()
    emp_id_list = []
    name_list = []
    email_list = []
    office_location_list = []
    department_list = []
    for each_emp in emp_data:
        emp_id_list.append(each_emp.id)
        name_list.append(each_emp.name)
        email_list.append(each_emp.email)
        office_location_list.append(each_emp.office_location)
        department_list.append(each_emp.department)

    context = {
        'emp_id_list': emp_id_list,
        'name_list': name_list,
        'email_list': email_list,
        'office_location_list': office_location_list,
        'department_list': department_list,
        'range': range(0, len(name_list)),
    }
    return render(request, 'emp_dashboard.html', context)
