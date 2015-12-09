import re
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.shortcuts import render, render_to_response, get_object_or_404, RequestContext
from beers_alt.models import Event
from beers_alt.models import Ingredient
from beers_alt.models import Part_Of
from beers_alt.models import Event_Ingredient
from beers_alt.models import Who_Buys
from django.contrib.auth.models import User
from .forms import EventForm
from .forms import InviteForm
from django.forms.models import ModelForm, inlineformset_factory
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from beers_alt.forms import UserCreationForm
from django.db import connection
import time
from django import forms
from django.db.models import Max

from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail, EmailMessage

from django.contrib.auth.models import User

class A:
    def __init__(self, eid1):
        self.eid = eid1




def welcome(request):
    return render(request, "beers_alt/welcome.html")

@login_required(login_url='/accounts/login/')
def home_page(request, current_user):
    cursor = connection.cursor()
    home_page = request.user.get_username() #get_object_or_404(Registered_User, pk=current_user)
    cursor.execute('SELECT Event.Title, Event.date, Event.time, Event.eid, EVENT.location, EVENT.description  FROM Auth_User, Part_Of, Event where part_of.id = Auth_User.id AND part_of.eid = event.eid and Auth_User.username = %s and Event.date >= %s ORDER BY Event.Date, EVENT.TIME', [request.user.get_username(), time.strftime("%d/%m/%Y")])
    rows = cursor.fetchall()
    cursor.execute('SELECT Event.Title, Event.date, Event.time, Event.eid, EVENT.location, EVENT.description FROM Auth_User, Part_Of, Event where part_of.id = Auth_User.id AND part_of.eid = event.eid and Auth_User.username = %s and Event.date < %s ORDER BY Event.Date, EVENT.TIME', [request.user.get_username(), time.strftime("%d/%m/%Y")])
    rows2 = cursor.fetchall()

    return render_to_response('beers_alt/home-page.html',
    { 'userinfo' : home_page,
      #'Events' : Registered_User.objects.raw('SELECT Registered_User.id, Registered_User.username FROM Registered_User WHERE Registered_User.username = %s', ['vada berkich']),
      'FutureEvents' : rows,
      'PastEvents' : rows2,

        },
        context_instance=RequestContext(request))

def login(request):
    return render_to_response('beers_alt/login.html',
        {},
        context_instance=RequestContext(request))

#incomplete/incorrect
# def get_event(request):
#     # if this is a POST request we need to process the form data
#     if request.method == 'POST':
#         # create a form instance and populate it with data from the request:
#         form = EventForm(request.POST)
#         # check whether it's valid:
#         if form.is_valid():
#             # process the data in form.cleaned_data as required
#             # ...
#             # redirect to a new URL:
#             return HttpResponseRedirect('/thanks/')
#
#     # if a GET (or any other method) we'll create a blank form
#     else:
#         form = EventForm()
#
#     return render(request, 'create-event.html', {'form': form})

@login_required(login_url='/accounts/login/')
def create_event(request):
    # title = forms.CharField(label=_("Title"), widget=forms.TextInput)
    if request.method =='POST':
        eform = EventForm(request.POST)
        if eform.is_valid():
            neweventid = eform.save().eid
            A.eid = neweventid
           

            #print neweventid

            #get current user's id who created the event
            current_user = request.user
            current_user_id = current_user.id
            #print current_user_id
            #to create new part of relation, increment uid
            intHolder = Part_Of.objects.all().aggregate(Max('uid'))['uid__max']
            intHolder += 1
            #print intHolder
            #insert intholder, current user id, and true for admin
            cursor = connection.cursor()
            cursor.execute('INSERT INTO Part_Of VALUES (%s, %s, %s, %s)', (intHolder, current_user_id, neweventid, True))
            return HttpResponseRedirect(reverse('beers_alt.views.invite_form')) #, args=(str(neweventid),)
    else:
        eform = EventForm()
    return render_to_response('beers_alt/create-event.html',
        { 'EventForm': eform,
          },
        context_instance=RequestContext(request))

@login_required(login_url='/accounts/login/')
def invite_form(request):
    # print "I love giraffffff so much it hurts"
    # print "++++++++++++"   
    # print A.eid
    # print "++++++++++++"   
    form = InviteForm()
    if request.method == 'POST':
        form = InviteForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            email = data.get('user_email')
            cursor = connection.cursor()
            #gathers all users who have the email address listed
            cursor.execute('SELECT id FROM auth_user WHERE email = %s', [email])
            FoundUserIDs = cursor.fetchall()

            #please don't freak out, this is giving us a list of user ids, trust me
            listOfIds = [] 
            for id9 in FoundUserIDs:
                listOfIds.append(id9[0])

            if len(listOfIds) > 0:
                intHolder = Part_Of.objects.all().aggregate(Max('uid'))['uid__max']
                for current_user_id in listOfIds:
                    intHolder += 1
                    cursor = connection.cursor()
                    cursor.execute('INSERT INTO Part_Of VALUES (%s, %s, %s, %s)', (intHolder, current_user_id, A.eid, False))

                #right now, do nothing, in 5 secs pls send email
            else:
                subject = 'CrowdCon Invitation'
                message = 'Someone has invited you to their event on CrowdCon!'
                msg = EmailMessage(subject, message, to=[email])
                msg.send()
                # subject = 'CrowdCon Invitation'
                # message = 'test message! jdfghkjfdhg'
                # from_email = settings.EMAIL_HOST_USER;
                # send_mail(subject, message, from_email, ['special.cg00@gmail.com'], fail_silently=False)
                #for loop through each, with its own cursor statement to add to part_of


            return HttpResponseRedirect(reverse('beers_alt.views.welcome'))
        print "not valid?"
    else:
        print "cat cat"
        form = InviteForm()
    return render_to_response('beers_alt/invite.html',
        { 'InviteForm': form },
        context_instance=RequestContext(request))


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse(('beers_alt.views.welcome')))
    else:
        form = UserCreationForm()
    return render_to_response('beers_alt/register.html',
        { 'form': form, },
        context_instance=RequestContext(request))

def logout(request):
    auth_logout(request)
    return HttpResponseRedirect(reverse('beers_alt.views.welcome'))

def all_drinkers(request):
    return render_to_response('beers_alt/all-drinkers.html',
        { 'drinkers': Drinker.objects.all().order_by('name'),
          'registered_users': User.objects.all().order_by('username'),
          'events': Event.objects.all().order_by('title'),
          'ingredients': Ingredient.objects.all().order_by('ingredient_name'),
          'part_ofs': Part_Of.objects.all().order_by('email'),
          'event_ingredients': Event_Ingredient.objects.all().order_by('name'),
          'who_buyss': Who_Buys.objects.all().order_by('email'),
          },
        context_instance=RequestContext(request))

def drinker(request, drinker_name):
    drinker = get_object_or_404(Drinker, pk=drinker_name)
    return render_to_response('beers_alt/drinker.html',
        { 'drinker' : drinker,
          # 'beers' : Beer.objects.raw('SELECT * FROM Beer WHERE name IN (SELECT beer FROM Likes WHERE drinker = %s) ORDER BY name', [drinker.name]),
        #   'beers' : Beer.objects.filter(likes__drinker__exact=drinker).order_by('name'),
        #   # 'frequents' : Frequents.objects.raw('SELECT * FROM Frequents WHERE drinker = %s ORDER BY bar', [drinker.name]),
        #   'frequents' : drinker.frequents_set.all().order_by('bar'),
        },
        context_instance=RequestContext(request))

def event(request, eid):
    event = get_object_or_404(Event, eid=eid)
    cursor = connection.cursor()
    cursor.execute('SELECT EVENT.title, EVENT.eid, EVENT_INGREDIENT.eid, EVENT_INGREDIENT.ingredient_name, EVENT_INGREDIENT.quantity, EVENT_INGREDIENT.units, EVENT_INGREDIENT.comments, WHO_BUYS.Bringing, Auth_User.username FROM EVENT, EVENT_INGREDIENT, WHO_BUYS, AUTH_USER WHERE EVENT.eid = EVENT_INGREDIENT.eid and EVENT.EID = %s and WHO_BUYS.id= Auth_User.id and WHO_BUYS.eid = EVENT.eid', [eid])
    rows = cursor.fetchall()
    return render_to_response('beers_alt/event.html',
        { 'event' : event,
          'ingredient' : rows,
        },
        context_instance=RequestContext(request))

# def registered_user(request, registered_username):
#     registered_user = get_object_or_404(Registered_User, pk=registered_username)
#     return render_to_response('beers_alt/user.html',
#         { 'registered_user' : registered_user,
#           # 'beers' : Beer.objects.raw('SELECT * FROM Beer WHERE name IN (SELECT beer FROM Likes WHERE drinker = %s) ORDER BY name', [drinker.name]),
#         #   'beers' : Beer.objects.filter(likes__drinker__exact=drinker).order_by('name'),
#         #   # 'frequents' : Frequents.objects.raw('SELECT * FROM Frequents WHERE drinker = %s ORDER BY bar', [drinker.name]),
#         #   'frequents' : drinker.frequents_set.all().order_by('bar'),
#         },
#         context_instance=RequestContext(request))

def edit_drinker(request, drinker_name):
    drinker = get_object_or_404(Drinker, pk=drinker_name)
    # beers = Beer.objects.all().order_by('name')
    # beersLiked = [(beer, Likes.objects.filter(drinker__exact=drinker, beer__exact=beer).exists())
    #               for beer in beers]
    # bars = Bar.objects.all().order_by('name')
    # frequents = Frequents.objects.filter(drinker__exact=drinker).all()
    # barsFrequented = [(bar, frequents.get(bar__exact=bar).times_a_week if frequents.filter(bar__exact=bar).exists() else 0)
    #                   for bar in bars]
    return render_to_response('beers_alt/edit-drinker.html',
        { 'drinker' : drinker,
        #   'beersLiked' : beersLiked,
        #   'barsFrequented' : barsFrequented,
        },
        context_instance=RequestContext(request))

def edit_drinker_submit(request, drinker_name):
    drinker = get_object_or_404(Drinker, pk=drinker_name)
    try:
        address = request.POST['address']
        beersLiked = [Beer.objects.get(pk=beerName)
                      for beerName in request.POST.getlist('BeersLiked')]
        barsFrequented = []
        for key, val in request.POST.items():
            m = re.match('^BarsFrequented/(?P<barName>.*)$', key)
            if m and int(val) > 0:
                barsFrequented.append((Bar.objects.get(pk=m.group('barName')), int(val)))
    except (KeyError):
        return render_to_response('beers_alt/edit-drinker.html',
            { 'drinker' : drinker_name,
              'error_message': "Input error!" },
            context_instance=RequestContext(request))
    else:
        drinker.address = address
        drinker.save()
        Likes.objects.filter(drinker__exact=drinker).delete()
        for beer in beersLiked:
            Likes(drinker=drinker, beer=beer).save()
        Frequents.objects.filter(drinker__exact=drinker).delete()
        for bar, times_a_week in barsFrequented:
            Frequents(drinker=drinker, bar=bar, times_a_week=times_a_week).save()
        # Always return an HttpResponseRedirect after successfully dealing with
        # POST data.  This prevents data from being posted twice if a user hits
        # the back button.
	return HttpResponseRedirect(reverse('beers_alt.views.drinker', args=(drinker.name,)))
