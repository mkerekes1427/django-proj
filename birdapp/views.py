from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.
def home(request):
    return render(request, "home.html")

def bird_email(request):

    if request.method == "POST":

        data = {}

        data["email"] = request.POST["email"]
        data["bird_count"] = request.POST["bird_count"]
        data["species"] = request.POST.getlist("species")
        data["message"] = request.POST["message"]

        return JsonResponse(data)

    return render(request, "bird_email.html")

def contact(request):
    return render(request, "contact.html")