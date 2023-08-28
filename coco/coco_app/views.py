from django.shortcuts import render, redirect
from .models import Time, Project
from django.contrib.auth.models import User
import datetime as dt

times_array = [
    {'date': '23.08.23', 'time': '4:30', 'project': 'Züri Fäscht', 'comments': 'much fun'},
    {'date': '24.08.23', 'time': '5:30', 'project': 'NKB', 'comments': 'very boring'},
    {'date': '25.08.23', 'time': '6:30', 'project': 'EHB', 'comments': 'pain in the ass'},
    {'date': '26.08.23', 'time': '7:30', 'project': 'Veriset', 'comments': 'sucks'},
]
# Create your views here.

def home_view(request):
    template = 'home.html'
    users = ['Townsend', 'Beth Harmon', 'Benny Fisher', 'Harry Beltik', 'Antonin Borgov']
    context = {'users': users, 'title': "Home"}
    return render(request, template, context)

def time_logger(request, time_id):
    projects = Project.objects.all()  # for <select>
    date = dt.date.today().strftime('%Y-%m-%d')
    time = {}
    template = 'time_logger.html'

    if request.method == 'POST':
        context = {'projects': projects, 'title': "Time Logger", 'date': date}
        return render(request, template, context)

    if request.method == 'GET':
        if time_id != 0:
            time = Time.objects.filter(id=time_id)[0]
            date = time.date.strftime('%Y-%m-%d')  # required to get date input to show
    context = {'template': template, 'time': time, 'date': date, 'projects': projects}
    return render(request, template, context)

def time_overview(request):
    times = Time.objects.filter(developer_id=2)
    template = 'time_overview.html'
    user = request.POST.get('selected_user')
    context = {'user': user, 'times': times, 'title': "Time Overview"}
    return render(request, template, context)

