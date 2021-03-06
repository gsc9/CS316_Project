from django import forms
from models import Event
from .models import Part_Of
from django.db.models import Max
from beers_alt.models import Event_Ingredient
from beers_alt.models import Who_Buys

from django.forms import EmailField

from django.utils.translation import ugettext_lazy as _

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


# class PartofForm(forms.Form):
# 	partof_id = forms.IntegerField()
# 	partof_eid = forms.IntegerField()
# 	partof_is_admin = forms.BooleanField()

# 	class Meta:
# 		model = Part_Of

# 	def save(self, commit=True):
# 		partof = super(PartofForm, self).save(commit=False)
# 		partof.id = partof_id
# 		partof.eid =

class UserCreationForm(UserCreationForm):
    email = EmailField(label=_("Email address"), required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


class EventForm(forms.ModelForm):
    # event_title = forms.CharField(label='Event Title', max_length=256)
    # event_date = forms.CharField(label='Date', max_length=100)
    # event_time = forms.CharField(label='Time', max_length=100)
    # event_location = forms.CharField(label='Location', max_length=256)
    # event_description = forms.CharField(label='Description', max_length=400)

    class Meta:
    	model = Event
    	fields = {"title", "date", "time", "location", "description"}

    def save(self, commit=True):
    	event = super(EventForm, self).save(commit=False)
    	# event.dd = int(Event.objects.all().aggregate(Max('eid'))[eid]) + 1
        intHolder = Event.objects.all().aggregate(Max('eid'))['eid__max']
        intHolder += 1
        event.eid = intHolder
    	# event.eid = forms.AutoField(primary_key=True)
    	# event.title = event_title
    	# event.date = event_date
    	# event.time = event_time
    	# event.location = event_location
    	# event.description = event_description
    	if commit:
    		event.save()
    	return event

#3 int and a boolean
class InviteForm(forms.Form):
    user_email = forms.CharField(label='User email', max_length=256)

# uid  |  id  |  ingredient_name   | eid  | bringing |                    user_comments
class BringForm(forms.Form):
    ingredient_name = forms.ModelChoiceField(Event_Ingredient.objects.all())
    quantity = forms.IntegerField()
    comments = forms.CharField(label='comments', max_length=300)

    def __init__(self,*args,**kwargs):
        my_arg = kwargs.pop('e_id')
        super(BringForm,self).__init__(*args,**kwargs)
        # self.fields['curr_eid'] = my_arg
        self.fields['ingredient_name'].queryset = (Event_Ingredient.objects.values_list('ingredient_name', flat=True).filter(eid=my_arg))

class AddForm(forms.Form):
    ingredient_name = forms.CharField(label='New Ingredient', max_length=300)
    quantity = forms.IntegerField()
    units = forms.CharField(label='Units', max_length=256)
    comments = forms.CharField(label='Comments', max_length=300)
