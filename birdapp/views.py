from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import User, Observation
from .my_validators import _password_good, _confirm_password, _bird_color
from .forms import ObservationForm

# Create your views here.
def home(request):
    return render(request, "home.html")


def login_user(request):
        
    if request.method == "POST":

        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)

        if user is not None:

            login(request, user)
            messages.add_message(request, messages.SUCCESS, "You are logged in")
            return redirect("home")
        
        else:
            messages.add_message(request, messages.WARNING, "Credentials are incorrect")

    return render(request, "login_user.html")

def logout_user(request):

    if request.method == "POST":

        try:
            logout(request)
            messages.add_message(request, messages.SUCCESS, "You're logged out")
        except:
            messages.add_message(request, messages.WARNING, "Could not log out")


    if not request.user.is_authenticated:
        return redirect("home")

    return render(request, "logout_user.html")

def signup(request):

    if request.method == "POST":

        unique_username = False

        username = request.POST["username"]
        password = request.POST["password"]
        confirm = request.POST["confirm"]

        try:
            users = User.objects.get(username = username)

        except User.DoesNotExist:
            unique_username = True
        
        if not unique_username:
            messages.add_message(request, messages.WARNING, "Choose a different username")

        elif not _password_good(password):
            messages.add_message(request, messages.WARNING, "Password doesn't meet requirements")
        
        elif not _confirm_password(password, confirm):
            messages.add_message(request, messages.WARNING, "Passwords don't match")

        else:

            new_user = User.objects.create_user(username=username, password=password)

            messages.add_message(request, messages.SUCCESS, "Your account was created")
            return redirect("login_user")

    return render(request, "signup.html")

def upload_observation(request):

    if not request.user.is_authenticated:
        return redirect("login_user")

    if request.method == "POST":

        color = _bird_color(request.POST["name"])

        new_observation = Observation(person=request.user, color=color)

        form = ObservationForm(request.POST, request.FILES, instance=new_observation)

        if form.is_valid():

            form.save()
            messages.add_message(request, messages.SUCCESS, "Observation was uploaded")

        else:
            print("Form not valid")
            print(form.errors)
            messages.add_message(request, messages.WARNING, "Error with upload")
        
        
    return render(request, "upload_observation.html")


def profile(request):


    if not request.user.is_authenticated:
        redirect("user_login")

    current_user = User.objects.get(id=request.user.id)

    render(request, "profile.html", context={"current" : current_user})


def bird_email(request):

    if request.method == "POST":
        return JsonResponse({"data" : request.POST})  

    categories = ["Songbird", "Raptor", "Water Bird"]

    return render(request, "bird_email.html", context={"categories" : categories})

def contact(request):

    if request.method == "POST":

        message = f"""

        {request.POST["name"]} emailed.

        Their email address is {request.POST["email"]}.

        Their message is {request.POST["message"]}
        
        """

        subject = request.POST["subject"]

        send_mail(subject, message, settings.EMAIL_HOST_USER, ["mkerekes53@gmail.com"], fail_silently=False)


    return render(request, "contact.html")


