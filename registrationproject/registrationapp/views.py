from django.shortcuts import render
from django.http.response import HttpResponse
from.models import RegistrationData



def home(request):
    return render(request,'home.html')


def login(request):
    if request.method=="POST":
        username=request.POST.get("username",'')
        password1=request.POST.get("password1",'')
        username=RegistrationData.objects.filter(username=username)
        password1=RegistrationData.objects.filter(password1=password1)
        if username and password1:
            return render(request,'home.html')
        else:
            return HttpResponse("<center><h1>Invalide Detalies<h1></center>")

    return render(request,'loginpage.html')


def registration(request):
    if request.method=="POST":
        rform=RegistrationData(request.POST)
        first_name=request.POST.get('first_name','')
        last_name=request.POST.get('last_name','')
        mobile=request.POST.get('mobile','')
        email=request.POST.get('email','')
        #date=request.POST.get('date','')
        user_name=request.POST.get('user_name','')
        password1=request.POST.get('password1','')
        password2=request.POST.get('password2','')
        data=RegistrationData(
            first_name=first_name,
            last_name=last_name,
            mobaile=mobile,
            email=email,
           # date=date,
            username=user_name,
            password1=password1,
            password2=password2,
        )
        data.save()
        rform=RegistrationData.objects.all()
        print(data)
        return render(request,"registration.html",{'rform':rform})
    else:
        rform=RegistrationData.objects.all()
        return render(request,"registration.html",{'rform':rform})


