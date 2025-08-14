from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect, get_object_or_404
from django.utils import timezone
from .models import Twit
from .forms import TwitForm

# Create your views here.

def home(request):
    return render(request, 'home.html')

def twit_list(request):
    twits = Twit.objects.all().order_by('-created_at')
    return render(request, 'twit_list.html', {'twits': twits})

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

def twit_delete(request, id):
    twit = get_object_or_404(Twit, pk=id, user=request.user)
    if request.method == 'POST':
        twit.delete()
        return redirect('twit_list')    
    return render(request, 'twit_delete.html', {'twit': twit})