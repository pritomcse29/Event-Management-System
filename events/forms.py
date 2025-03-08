from django import forms
from events.models import Event, Category 
from django.contrib.auth.models import User

class EventModelForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'description', 'date', 'time', 'location', 'category','asset']
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
class ParticipantForm(forms.ModelForm):
    events = forms.ModelMultipleChoiceField(
        queryset=Event.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'events']
# class ParticipantModelForm(forms.ModelForm):
#     participants = forms.ModelMultipleChoiceField(
#         queryset=User.objects.all(),
#         widget=forms.CheckboxSelectMultiple(attrs={'class': 'border rounded-md p-2 w-full mb-3'}),
#         required=True
#     )

#     class Meta:
#         model = Event
#         fields = ['participants']

# class ParticipantModelForm(forms.ModelForm):
#     participants  = forms.ModelMultipleChoiceField(
#         queryset =  User.objects.all(),
#         widget = forms.CheckboxSelectMultiple(attrs={'class': 'border rounded-md p-2 w-full mb-3'}),
#         required = True
#     )
#     class Meta:
#         model = Event
#         fields = ['participants']
    # event = forms.ModelChoiceField(
    #     queryset=Event.objects.all(),
    #     widget=forms.Select,  
    #     required=True
    # )
    # name = forms.CharField(
    #     max_length=100, 
    #     widget=forms.TextInput(attrs={'class': 'border rounded-md p-2 w-full mb-3'}),
    #     required=True
    # )
    # email = forms.EmailField(
    #     widget=forms.EmailInput(attrs={'class': 'border rounded-md p-2 w-full mb-3'}),
    #     required=True
    # )
    
    # class Meta:
    #     model = Event
    #     fields = ['name', 'email', 'event']

# class ParticipantModelForm(forms.ModelForm):
#     event = forms.ModelMultipleChoiceField(
#         queryset=Event.objects.all(),
#         widget=forms.CheckboxSelectMultiple,  
#         required=False
#     )
#     class Meta:
#         model = Event
#         fields = ['name', 'email','event']
#         widgets = {
#             'name': forms.TextInput(attrs={'class': 'border rounded-md p-2 w-full mb-3'}),
#             'email': forms.EmailInput(attrs={'class': 'border rounded-md p-2 w-full mb-3'})
#         }


