from beers_alt.models import Event, Ingredient, Part_Of, Event_Ingredient, Who_Buys
from django.contrib import admin

admin.site.register(Event)
admin.site.register(Ingredient)
admin.site.register(Part_Of)
admin.site.register(Event_Ingredient)
admin.site.register(Who_Buys)
