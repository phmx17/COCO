from django.shortcuts import render, redirect
from .models import Time, Project
from django.contrib.auth.models import User
import datetime as dt
from django.core.paginator import Paginator

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
    page = request.GET.get('page')
    template = 'time_overview.html'

    # calculate times for various calendar time spans
    def get_time_totals(period_query_set):
        time_total = 0.0
        for time_item in period_query_set:
            time_total += time_item.time
        return time_total

    time_rows = Time.objects.filter(developer__username='anya102').order_by('date')

    # total times worked ever
    time_totals = get_time_totals(time_rows)

    # current project totals
    current_project = time_rows.values_list('project__title').reverse()[0][0]  # get element from last project worked on and first element of the tuple
    time_totals_project = time_rows.filter(project__title=current_project)
    time_totals_project = get_time_totals(time_totals_project)

    # current week totals
    current_week = dt.date.today().strftime("%V") # OR: .isocalendar()[1]
    current_week_times = time_rows.filter(date__week=current_week)  # get times by month
    time_totals_week = get_time_totals(current_week_times)

    # current month totals
    current_month = dt.date.today().strftime('%m')
    current_month_times = time_rows.filter(date__month=current_month)  # get times by month
    time_totals_month = get_time_totals(current_month_times)

    # pack times into paginator
    paginator = Paginator(time_rows, 8)
    page_obj = paginator.get_page(page)

    context = {
        'times': time_rows,
        'time_totals': time_totals,
        'time_totals_project': time_totals_project,
        'time_totals_week': time_totals_week,
        'time_totals_month': time_totals_month,
        'title': "Times Overview", 'page_obj': page_obj}

    return render(request, template, context)

