from django import forms
from schedule.models import Event

class EventForm(forms.ModelForm):
    
    class Meta:
        model = Event
        fields = ("title","start_time","end_time","memo")
