from django import forms
from models import Event
from .models import Part_Of
from django.db.models import Max

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
    	# event.eid = int(Event.objects.all().aggregate(Max('eid'))[eid]) + 1
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
