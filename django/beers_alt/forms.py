from django import forms

class EventForm(forms.Form):
    event_title = forms.CharField(label='Event Title', max_length=256)
    event_date = forms.CharField(label='Date', max_length=100)
    event_time = forms.CharField(label='Time', max_length=100)
    event_location = forms.CharField(label='Your name', max_length=256)
