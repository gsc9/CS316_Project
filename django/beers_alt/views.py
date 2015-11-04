import re
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from beers_alt.models import Beer, Bar, Drinker, Frequents, Likes

def all_drinkers(request):
    return render_to_response('beers_alt/all-drinkers.html',
        { 'drinkers': Drinker.objects.all().order_by('name') },
        context_instance=RequestContext(request))

def drinker(request, drinker_name):
    drinker = get_object_or_404(Drinker, pk=drinker_name)
    return render_to_response('beers_alt/drinker.html',
        { 'drinker' : drinker, 
          # 'beers' : Beer.objects.raw('SELECT * FROM Beer WHERE name IN (SELECT beer FROM Likes WHERE drinker = %s) ORDER BY name', [drinker.name]),
          'beers' : Beer.objects.filter(likes__drinker__exact=drinker).order_by('name'),
          # 'frequents' : Frequents.objects.raw('SELECT * FROM Frequents WHERE drinker = %s ORDER BY bar', [drinker.name]),
          'frequents' : drinker.frequents_set.all().order_by('bar'),
        },
        context_instance=RequestContext(request))

def edit_drinker(request, drinker_name):
    drinker = get_object_or_404(Drinker, pk=drinker_name)
    beers = Beer.objects.all().order_by('name')
    beersLiked = [(beer, Likes.objects.filter(drinker__exact=drinker, beer__exact=beer).exists())
                  for beer in beers]
    bars = Bar.objects.all().order_by('name')
    frequents = Frequents.objects.filter(drinker__exact=drinker).all()
    barsFrequented = [(bar, frequents.get(bar__exact=bar).times_a_week if frequents.filter(bar__exact=bar).exists() else 0)
                      for bar in bars]
    return render_to_response('beers_alt/edit-drinker.html',
        { 'drinker' : drinker,
          'beersLiked' : beersLiked,
          'barsFrequented' : barsFrequented,
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
