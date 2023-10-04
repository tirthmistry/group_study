from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from django.db import IntegrityError
from .models import assignments_to_uploads

# Create your views here.
def home_page(request):
    data=assignments_to_uploads.objects.all()
    return render(request,"home.html",{"data":data})

def Assignment_page(request):
    data=assignments_to_uploads.objects.all()
    return render(request,"Assignment.html",{"data":data})

def detail(request,assign_id):
    data= get_object_or_404(assignments_to_uploads,pk=assign_id)
    return render(request,'details.html',{"data":data})

def signupaccount(request):
    if request.method=="GET":
        return render(request,"signup.html",{"form":UserCreationForm})
    else:
        if request.POST["password1"]==request.POST["password2"]:
            try:
                user=User.objects.create_user(request.POST["username"],password=request.POST["password1"])
                user.save()
                login(request,user)
                return redirect(loginaccount)
            except IntegrityError:
                return render(request,"signup.html",{"form":UserCreationForm,"error":"user name has already been taken"})
        else:
            return render(request,"signup.html",{"form":UserCreationForm,"error":"password must be same"})
  
def loginaccount(request):
    if request.method=="GET":
        return render(request,"login.html",{"form":AuthenticationForm})
    else:
        user=authenticate(request,username=request.POST["username"],password=request.POST["password"])
        if user is None:
            return render(request,"login.html",{"form":AuthenticationForm,"error":"user doesnt exist"})
        else:
            login(request,user)
            return redirect(home_page)

def logoutaccount(request):
    logout(request)
    return redirect(home_page)

def upload_assignment(request):
    if request.method=="POST":
        img1=request.FILES['image1']
        img2=request.FILES['image2']
        img3=request.FILES['image3']
        img4=request.FILES['image4']
        img5=request.FILES['image5']
        title=request.POST.get("title")
        desc=request.POST.get("description")
        upload_to_server=assignments_to_uploads(a_img1=img1,a_img2=img2,a_img3=img3,a_img4=img4,a_img5=img5,a_title=title,a_description=desc)
        upload_to_server.save()
    return render(request,"upload_assignment.html")