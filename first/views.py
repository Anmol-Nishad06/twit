from django.shortcuts import render
from django.shortcuts import redirect, get_object_or_404
from django.utils import timezone
from .models import Twit,Profile
from .forms import TwitForm , CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.db.models.signals import post_save
from django.contrib.auth.models import User


for user in User.objects.all():
    Profile.objects.get_or_create(user=user)

# Create your views here.

def home(request):
    return render(request, 'home.html')

def twit_list(request):
    twits = Twit.objects.all().order_by('-created_at')
    return render(request, 'twit_list.html', {'twits': twits})


@login_required
def twit_create(request):
    if request.method == 'POST':
        form = TwitForm(request.POST, request.FILES)
        if form.is_valid():
            twit = form.save(commit=False)
            twit.user = request.user
            twit.save()
            return redirect('twit_list')
    else:
        form = TwitForm()
    return render(request, 'twit_form.html', {'form': form})


@login_required
def twit_edit(request, id):
    twit = get_object_or_404(Twit, pk=id , user=request.user)
    if request.method == 'POST':
        form = TwitForm(request.POST, request.FILES, instance=twit) 
        if form.is_valid():
            form.save()
            twit.updated_at = timezone.now()
            twit.save()
            return redirect('twit_list')
    else:
        form = TwitForm(instance=twit)  
    return render(request, 'twit_form.html', {'form': form, 'twit': twit})


@login_required
def twit_delete(request, id):
    twit = get_object_or_404(Twit, pk=id, user=request.user)
    if request.method == 'POST':
        twit.delete()
        return redirect('twit_list')    
    return render(request, 'twit_delete.html', {'twit': twit})

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('twit_list')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    
post_save.connect(create_profile, sender=User)

@login_required
def profile(request):
    profile = get_object_or_404(Profile, user__username=request.user.username)
    twits = Twit.objects.filter(user=profile.user).order_by('-created_at')


    return render(request, 'profile.html', {'profile':profile, 'twits': twits})