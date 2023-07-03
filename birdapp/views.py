from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def home(request):
    return render(request, "home.html")

def upload_observation(request):

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