from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect  # 404 == great shortcut
from django.contrib import messages
from django.contrib.auth.models import Group, User

# custom
from .decorators import unauthenticated_user, allowed_users
from .forms import CreateUserForm


@unauthenticated_user
def login_page(request):
    template = 'auth/login.html'
    title = "Login"
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('test')
        else:
            messages.info(request, 'Incorrect username or password.')
    context = {'title': title}
    return render(request, template, context)

def logout_user(request):
    logout(request)
    return redirect('login')

@unauthenticated_user
def register(request):
    template = 'auth/register.html'
    form = CreateUserForm()  # initialize
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():  # own serializer
            form.save()
            username = form.cleaned_data.get('username')
            # add developer group by default
            user = User.objects.get(username=username)
            dev_group = Group.objects.get(name="developer")
            dev_group.user_set.add(user)
            messages.success(request, f"Account created for {username}.")  # print success message
            return redirect('login')
    context = {'form': form}
    return render(request, template, context)

def not_authorized(request):
    template = 'auth/not_authorized.html'
    title = "Not Authorized"
    message = 'You are not authorized to view this page.'
    context = {'title': title, 'message': message}
    return render(request, template, context)

def home(request):
    template = 'auth/home.html'
    title = 'Home'
    context = {'title': title}
    return render(request, template, context)

@login_required(login_url='login') # immediate redirect if not authenticated
@allowed_users(allowed_roles=['developer'])
def test(request):
    template = 'auth/test.html'
    title = "Test"
    context = {'title': title, }
    return render(request, template, context)