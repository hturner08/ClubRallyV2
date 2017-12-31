from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import UserForm
from .forms import CreateClubForm
from .models import Club
from .models import User
from django.forms import ModelForm
# Create your views here.

#FrontPage
def front(request):
    club_list = Club.objects.all()
    return render(request, 'clubs/index.html', {'club_list':club_list})
#AboutUs
def about(request):
    return render(request,'clubs/about.html')
def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserForm()
    return render(request, 'clubs/signup.html', {'form': form})
def viewUser(request, user_id):
    return HttpResponse("You cannot currently view users(I hate coding those fucking django templates so this feature is not happening for now).")
#Search Clubs
def home(request):
    if(request.user.is_authenticated):
        club_list = Club.objects.all()
        return render(request, 'clubs/clubs.html',{'club_list':club_list})
    return HttpResponse("You do not have access to this page")

#My Clubs
def index(request):
    if(request.user.is_authenticated):
        club_list = request.user.current_clubs.all()
        return render(request,'clubs/myclubs.html',{'club_list':club_list})
    return HttpResponse("You do not have access to this page")

def createClub(request):
    if request.method == 'POST':
        form = CreateClubForm(request.POST)
        if form.is_valid():
            form.save()
            club_id = form.cleaned_data.get('id')
            return redirect('clubs:index')
    else:
        form = CreateClubForm()
    return render(request, 'clubs/createclub.html',{'form':form})

def editClub(request,club_id):
    club = get_object_or_404(Club,pk=club_id)
    if(request.user.is_authenticated & (club.presidents.filter(email=request.user.email).exists())):
        if request.method == 'POST':
            form = CreateClubForm(request.POST,instance=club)
            if form.is_valid():
                form.save()
                return redirect('clubs:index')
        else:
            form = CreateClubForm(instance=club)
            return render(request,'clubs/editclub.html',{'form':form})
    return HttpResponse("You do not have permission to edit this club")

#Specific Club
def detail(request, club_id):
    if(request.user.is_authenticated):
        theCluuuuub = get_object_or_404(Club,pk=club_id)
        return render(request, 'clubs/detail.html',{'club' : theCluuuuub})
    return HttpResponse("You do not have access to this page")
    #Yes that was a Key&Peele reference, and yes it took me 4 tries to get the Us right when I called the variable again
def join(request, club_id):
    club = get_object_or_404(Club,pk=club_id)#making sure club exists
    if(request.user.is_authenticated):
        if not request.user.current_clubs.filter(pk=club_id).exists():
            request.user.add_club(club_id)
            return redirect('home')
    return HttpResponse("Something went wrong...")
