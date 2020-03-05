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

    ingreds = []
    ilist = dinner_list.objects.all()
    
    for item in ilist:
        if item.name == hlist[-7]:
            ingreds.append(item.ingredients)
        elif item.name == hlist[-6]:
            ingreds.append(item.ingredients)
        elif item.name == hlist[-5]:
            ingreds.append(item.ingredients)
        elif item.name == hlist[-4]:
            ingreds.append(item.ingredients)
        elif item.name == hlist[-3]:
            ingreds.append(item.ingredients)
        elif item.name == hlist[-2]:
            ingreds.append(item.ingredients)
        elif item.name == hlist[-1]:
            ingreds.append(item.ingredients)
        else:
            pass

    ingred =[]
    for item in ingreds:
        item = item.split(",")
        ingred.extend(item)
   
    
    #assign last 7 entries to var for rendering to home page.
    mon = hlist[-7]
    tues = hlist[-6]
    wed = hlist[-5]
    thurs = hlist[-4]
    fri = hlist[-3]
    sat = hlist[-2]
    sun = hlist[-1]

    return render(request, 'food/home.html', {'mon':mon, 'tues':tues, 'wed':wed, 'thurs':thurs, 'fri':fri, 'sat':sat, 'sun':sun, 'ingred':ingred})


def addreceipe(request):
    form = addreceipeform(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'food/add.html', {'form':form})