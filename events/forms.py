from django import forms
from events.models import Event, Category , Participant

class EventModelForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'description', 'date', 'time', 'location', 'category']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'border rounded-md p-2 w-full mb-3'}),
            'description': forms.Textarea(attrs={'class': 'border rounded-md p-2 w-full mb-3', 'rows': 3}),
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'border rounded-md p-2 w-full mb-3'}),
            'time': forms.TimeInput(attrs={'type': 'time', 'class': 'border rounded-md p-2 w-full mb-3'}),
            'location': forms.TextInput(attrs={'class': 'border rounded-md p-2 w-full mb-3'}),
            'category': forms.Select(attrs={'class': 'border rounded-md p-2 w-full mb-3'}),
        }

class CategoryModelForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'border rounded-md p-2 w-full mb-3'}),
            'description': forms.Textarea(attrs={'class': 'border rounded-md p-2 w-full mb-3', 'rows': 3}),
        }

class ParticipantModelForm(forms.ModelForm):
    event = forms.ModelMultipleChoiceField(
        queryset=Event.objects.all(),
        widget=forms.CheckboxSelectMultiple,  
        required=False
    )
    class Meta:
        model = Participant
        fields = ['name', 'email','event']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'border rounded-md p-2 w-full mb-3'}),
            'email': forms.EmailInput(attrs={'class': 'border rounded-md p-2 w-full mb-3'})
        }


