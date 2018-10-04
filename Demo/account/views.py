from django.shortcuts import render,reverse
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login
from .models import UserProfile
from .forms import RegisterForm,UserProfileForm,LoginForm,UserForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.

def register(request):
    if request.method == "POST":
        user_form = RegisterForm(request.POST)
        userprofile_form = UserProfileForm(request.POST)

        if user_form.is_valid() * userprofile_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            userprofile = userprofile_form.save(commit=False)
            userprofile.user = new_user
            userprofile.save()
            return HttpResponseRedirect(reverse("account:RegisterSuccess"))
        else:
            return HttpResponseRedirect(reverse("account:RegisterFailure"))

    if request.method == "GET":
        user_form = RegisterForm()
        userprofile_form = UserProfileForm()
        return render(request,'account/register.html',{'user_form':user_form,"userprofile_form":userprofile_form})


def user_login(request):
    if request.method == "POST":
        user_form = LoginForm(request.POST)
        if user_form.is_valid():
            cd = user_form.cleaned_data
            user = authenticate(username=cd['username'],password=cd['password'])
            if user:
                login(request,user)
                return HttpResponse("Successful!")
            else:
                return HttpResponse("You can not login!")
        else:
            return HttpResponse("Input not valid!")

    if request.method == "GET":
        user_form = LoginForm()
        return render(request,"account/login.html",{"form":user_form})

def success(request):
    return render(request,"account/registerSuccess.html")


def failure(request):
    return render(request,"account/registerfailture.html")


@login_required(login_url='/account/login/')
def myself(request):
    user = User.objects.get(username=request.user.username)
    userprofile = UserProfile.objects.get(user=user)
    return render(request,"account/myself.html",{"user":user,"userprofile":userprofile})

@login_required(login_url='/account/login/')
def editmyself(request):
    user = User.objects.get(username=request.user.username)
    userprofile = UserProfile.objects.get(user=user)

    if request.method == "POST":
        user_form = UserForm(request.POST)
        userprofile_form = UserProfileForm(request.POST)
        if user_form.is_valid() * userprofile_form.is_valid():
            user_cd = user_form.cleaned_data
            userprofile_cd = userprofile_form.cleaned_data
            user.email = user_cd['email']
            userprofile.RealName = userprofile_cd['RealName']
            userprofile.School = userprofile_cd['School']
            userprofile.SchoolNumber = userprofile_cd['SchoolNumber']
            userprofile.Class = userprofile_cd['Class']
            userprofile.phone = userprofile_cd['phone']
            user.save()
            userprofile.save()
            return HttpResponseRedirect('/account/myself')

    if request.method == "GET":
        user_form = UserForm(instance=request.user)
        userprofile_form = UserProfileForm(initial={"SchoolNumber":userprofile.SchoolNumber,"School":userprofile.School,"Class":userprofile.Class,"RealName":userprofile.RealName,"phone":userprofile.phone})
        return render(request,"account/editmyself.html",{"user_form":user_form,"userprofile_form":userprofile_form})


@login_required(login_url="/account/login")
def my_image(request):
    if request.method == "POST":
        img = request.POST['img']
        userprofile = UserProfile.objects.get(user=request.user.id)
        userprofile.photo = img
        userprofile.save()
        return HttpResponse("1")
    else:
        return render(request,"account/imagecrop.html")