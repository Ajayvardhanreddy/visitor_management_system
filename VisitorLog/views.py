from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from .models import Visitor
from datetime import date
from django import template
from django.contrib import messages

register = template.Library()


# Create your views here.
def home(request):
    return render(request, 'VisitorLog.html')


def add_visitor(request):
    if request.method == "POST":
        visitor_name = request.POST.get('visitor_name')
        email = request.POST.get('email')
        mobile_no = request.POST.get('mobile_no')
        office_location = request.POST.get('office_location')
        visitor_host = request.POST.get('visitor_host')
        visitor_status = request.POST.get('visitor_status')


        current_time = datetime.now().strftime("%H:%M:%S")
        today_date = date.today().strftime("%Y-%m-%d")


        print(visitor_name, email, mobile_no, office_location, visitor_host, visitor_status, current_time, today_date)
        obj = Visitor(
            visitor_name=visitor_name,
            email=email,
            mobile_no=mobile_no,
            office_location=office_location,
            visitor_host=visitor_host,
            arrival_time=current_time,
            arrival_date=today_date,
            departure_time=None,
            departure_date=None,
            visitor_status=visitor_status
        )
        obj.save()
        return HttpResponse("Employee Data Successfully added!")
    return render(request, 'add_visitor.html')


def visitor_dashboard(request):
    visitor_data = Visitor.objects.all()
    visitor_id_list = []
    visitor_name_list = []
    visitor_email_list = []
    mobile_no_list = []
    office_location_list = []
    visitor_host_list = []
    arrival_time_list = []
    arrival_date_list = []
    departure_time_list = []
    departure_date_list = []
    visitor_status_list = []

    for each_visitor in visitor_data:
        visitor_id_list.append(each_visitor.id)
        visitor_name_list.append(each_visitor.visitor_name)
        visitor_email_list.append(each_visitor.email)
        mobile_no_list.append(each_visitor.mobile_no)
        office_location_list.append(each_visitor.office_location)
        visitor_host_list.append(each_visitor.visitor_host)
        arrival_time_list.append(each_visitor.arrival_time)
        arrival_date_list.append(each_visitor.arrival_date)
        departure_time_list.append(each_visitor.departure_time)
        departure_date_list.append(each_visitor.departure_date)
        visitor_status_list.append(each_visitor.visitor_status)

    context = {
        'visitor_id_list': visitor_id_list,
        'visitor_name_list': visitor_name_list,
        'visitor_email_list': visitor_email_list,
        'mobile_no_list': mobile_no_list,
        'office_location_list': office_location_list,
        'visitor_host_list': visitor_host_list,
        'arrival_time_list': arrival_time_list,
        'arrival_date_list': arrival_date_list,
        'departure_time_list': departure_time_list,
        'departure_date_list': departure_date_list,
        'visitor_status_list': visitor_status_list,
        'range': range(0, len(visitor_name_list)),
    }
    return render(request, 'visitor_dashboard.html', context)


def update_visitor_status(request, visitor_id):
    obj = Visitor.objects.get(id=visitor_id)
    context = {
        'visitor_name': obj.visitor_name,
        'visitor_id': visitor_id
    }
    return render(request, 'update_visitor_status.html', context)


def update_status(request):
    if request.method == "POST":
        visitor_id = request.POST.get('visitor_id')
        visitor_name = request.POST.get('visitor_name')
        visitor_status = request.POST.get('visitor_status')
        obj = Visitor.objects.get(id=visitor_id)
        obj.visitor_status = visitor_status
        if visitor_status == "Checked Out":
            current_time = datetime.now().strftime("%H:%M:%S")
            today_date = date.today().strftime("%Y-%m-%d")
            obj.departure_time = current_time
            obj.departure_date = today_date
        obj.save()
        return HttpResponse('Visitor Status Updated!')


def delete_visitor(request, visitor_id):
    try:
        record = Visitor.objects.get(id=visitor_id)
        record.delete()
        return HttpResponse("Visitor Record Deleted")
    except:
        return HttpResponse("Visitor doesn't exist!")