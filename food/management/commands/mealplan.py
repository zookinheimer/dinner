from django.core.management.base import BaseCommand
from food.models import history, dinner_list
import random
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings

class Command(BaseCommand):
    help = 'sends a weekly meal Plan'

    def handle(self, *args, **kwargs):
        #define lists to pull from
        dlist =[]
        hlist = []

        dtlist = dinner_list.objects.all()
        for item in dtlist:
            dlist.append(item.name)
        
        htlist = history.objects.all()
        for item in htlist:
            hlist.append(item.name)

        
        #check size of history and remove oldest entry if over 14 days then pick a random meal for day of week.
        while len(hlist) > 14:
            history.objects.filter(name = hlist[0]).delete()
            hlist.pop(0)
        mon = random.choice(dlist)
        while mon in hlist:
            mon = random.choice(dlist)
        h1 = history(name=mon)
        hlist.append(mon)
        h1.save()

        while len(hlist) > 14:
            history.objects.filter(name = hlist[0]).delete()
            hlist.pop(0)
        tues = random.choice(dlist)
        while tues in hlist:
            tues = random.choice(dlist)
        h2 = history(name=tues)
        hlist.append(tues)
        h2.save()

        while len(hlist) > 14:
            history.objects.filter(name = hlist[0]).delete()
            hlist.pop(0)
        wed = random.choice(dlist)
        while wed in hlist:
            wed = random.choice(dlist)
        h1 = history(name=wed)
        hlist.append(wed)
        h1.save()

        while len(hlist) > 14:
            history.objects.filter(name = hlist[0]).delete()
            hlist.pop(0)
        thurs = random.choice(dlist)
        while thurs in hlist:
            thurs = random.choice(dlist)
        h1 = history(name=thurs)
        hlist.append(thurs)
        h1.save()

        while len(hlist) > 14:
            history.objects.filter(name = hlist[0]).delete()
            hlist.pop(0)
        fri = random.choice(dlist)
        while fri in hlist:
            fri = random.choice(dlist)
        h1 = history(name=fri)
        hlist.append(fri)
        h1.save()

        while len(hlist) > 14:
            history.objects.filter(name = hlist[0]).delete()
            hlist.pop(0)
        sat = random.choice(dlist)
        while sat in hlist:
            sat = random.choice(dlist)
        h1 = history(name=sat)
        hlist.append(sat)
        h1.save()

        while len(hlist) > 14:
            history.objects.filter(name = hlist[0]).delete()
            hlist.pop(0)
        sun = random.choice(dlist)
        while sun in hlist:
            sun = random.choice(dlist)
        h1 = history(name=sun)
        hlist.append(sun)
        h1.save()

        subject='Meal Plan for the week'
        body = render_to_string('food/test.html', {'mon':mon, 'tues':tues, 'wed':wed, 'thurs':thurs, 'fri':fri, 'sat':sat, 'sun':sun})
        email = EmailMessage(subject, body, 'alex.cornelius@nwlogistics.com', ['alex.cornelius@nwlogistics.com', 'bethcornelius01@gmail.com'])
        email.content_subtype = 'html'
        email.send()
       