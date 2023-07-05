from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from .models import User, Observation

# Create your views here.
def home(request):
    return render(request, "home.html")


def login(request):
        
    if request.method == "POST":
        messages.add_message(request, messages.SUCCESS, "You are logged in")
        return redirect("home")

    return render(request, "login.html")

def logout(request):
    return render(request, "logout.html")

def signup(request):

    if request.method == "POST":
        messages.add_message(request, messages.SUCCESS, "Your account was created")
        return redirect("login")

    return render(request, "signup.html")

def upload_observation(request):

    if not request.user.is_authenticated:
        return redirect("login")

    # validate the date with form and use form.save() and model forms

    if request.method == "POST":
        return JsonResponse({"data" : request.POST})

    return render(request, "upload_observation.html")


def bird_email(request):

    if request.method == "POST":
        return JsonResponse({"data" : request.POST})  

    categories = ["Cardinal", "Corvids", "Hawks", "Falcons", "Owls",
                  "Warblers", "Water Birds"]

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