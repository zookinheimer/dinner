from django.shortcuts import render, redirect
import random
from .models import history, dinner_list
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from .forms import addreceipeform

# Create your views here.
def home(request): 
    hlist = []
    htlist = history.objects.all()
    for item in htlist:
        hlist.append(item.name)
    
    #assign last 7 entries to var for rendering to home page.
    mon = hlist[-7]
    tues = hlist[-6]
    wed = hlist[-5]
    thurs = hlist[-4]
    fri = hlist[-3]
    sat = hlist[-2]
    sun = hlist[-1]

    return render(request, 'food/home.html', {'mon':mon, 'tues':tues, 'wed':wed, 'thurs':thurs, 'fri':fri, 'sat':sat, 'sun':sun})


def addreceipe(request):
    form = addreceipeform(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'food/add.html', {'form':form})