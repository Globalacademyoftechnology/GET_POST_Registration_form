from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
# Create your views here.

def get_demo(request):
    name=request.GET.get("names")
    return render(request,"get_demo.html",{"name":name})


def post_demo(request):
    if request.method=="POST":
        name=request.POST.get('name')
        return HttpResponse("<h1>Thanks for submission Ms. {} </h1>".format(name))
    return render(request,"post_demo.html")



def register(request):
    if request.method=="POST":
        firstname=request.POST.get("first_name")
        lastname=request.POST.get("last_name")
        email=request.POST.get("email")
        phone_number=request.POST.get("phno")
        password=request.POST.get("pwd")
        Day=request.POST.get("birthday_day")
        Month=request.POST.get("birthday_month")
        Year=request.POST.get("birthday_year")
        Gender=request.POST.get("sex")
        if Gender=="1":
            Gender="Female"
        else:
            Gender="Male"
        send_mail("Thanks For Registration","hello Mr./Ms.{} {}\n Thanks for Registering".format(firstname,lastname),
        "djangosneha2119@gmail.com",[email,],fail_silently=False)

    return render(request,"myapp/registration.html")



