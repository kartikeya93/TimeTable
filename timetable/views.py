from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from timetable.forms import UserForm, UserProfileForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from . models import TimeTable
import datetime
import calendar


def index(request):
    return render(request, 'timetable/home.html')
# Create your views here.


def signup(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()

            user.set_password(user.password)
            user.is_active = True
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            registered = True
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request, 'timetable/signup.html', {'user_form': user_form, 'profile_form': profile_form,
                            'registered': registered})


def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                return render(request, 'timetable/inactive_user.html', {})

        else:
            return render(request, 'timetable/wrong_credentials.html', {})
    else:
        return render(request, 'timetable/login.html', {})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')


@login_required
def timetable(request):

    user = request.user.username
    temp = User.objects.get(username =user)
    rows = TimeTable.objects.filter(user=temp).filter(DateToday__gte=datetime.datetime.now())

    details = []

    for row in rows:
        row_detail = {}
        row = str(row).split(' ')
        row_detail["user"] = row[0]
        row_detail["date"] = datetime.datetime.strptime(row[1], '%Y-%m-%d').strftime('%d, %b %Y')
        row_detail["day"] = datetime.datetime.strptime(row[1], '%Y-%m-%d').weekday()
        row_detail["day"] = calendar.day_name[row_detail["day"]]
        row_detail["Period1"] = row[2]
        row_detail["Period2"] = row[3]
        row_detail["Period3"] = row[4]
        row_detail["Period4"] = row[5]
        row_detail["Period5"] = row[6]
        row_detail["Period6"] = row[7]
        row_detail["Period7"] = row[8]
        details.append(row_detail)

    if details == []:
        return render(request, 'timetable/timetable_empty.html')
    else:
        return render(request, 'timetable/timetable.html', {"details": details})








