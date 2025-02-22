from django.shortcuts import render,HttpResponse,redirect
from events.models import *
from events.forms import *
from datetime import date
from django.db.models import Q, Count, Max,Min,Avg
from django.urls import reverse

def dashboard(request):
    categories = Category.objects.all()  
    event = Participant.objects.all()

    type = request.GET.get('type', 'all')
    today = date.today()
    events = Event.objects.all()  
    today_events = Event.objects.filter(date=today)
    past_events = Event.objects.filter(date__lt=today).order_by('-date')
    upcoming_events = Event.objects.filter(date__gt=today).order_by('date')

    pubs = Participant.objects.aggregate(unique_count=Count('id', distinct=True))['unique_count']

  
    counts = Event.objects.aggregate(
        total=Count('id'),
        today_events=Count('id', filter=Q(date=today)),
        upcoming_events=Count('id', filter=Q(date__gt=today)),
        past_events=Count('id', filter=Q(date__lt=today))
    )

    base_query = Event.objects.prefetch_related('event').select_related('category')
    
    if type == 'today_events':
        events = base_query.filter(date=today)
    elif type == 'upcoming_events':
        events = base_query.filter(date__gt=today)
    elif type == 'past_events':
        events = base_query.filter(date__lt=today)
    elif type == 'pubs':
          events = Event.objects.filter(event__isnull=False).distinct()
    else:
        events = base_query.all()
    

    context = {
        'events': events,
        'counts': counts,
        'pubs':pubs,
        'events': events, 
        'today': today,
        'categories': categories,
        'event':event,
        
    }

    return render(request, 'dashboard/dashboard.html', context)
     

def create_event(request):
     event_e = EventModelForm()
     if request.method == "POST":
        event_e  = EventModelForm(request.POST)
        if event_e.is_valid():
                event_e.save()
                return redirect('dashboard')
    
        else:
            event_e =  EventModelForm()
            
     return render(request,'dashboard/create_event.html',{"event_e": event_e})
     
def create_category(request):
     event_form = CategoryModelForm()
     if request.method == "POST":
        event_form = CategoryModelForm(request.POST)
        if event_form.is_valid():
                event_form.save()
               
                return render(request,'dashboard/create_category.html',{"event_form":event_form,"message": "added successfully"})  
    
        else:
           event_form = CategoryModelForm()

     return render(request,'dashboard/create_category.html',{"event_form": event_form})
def create_participant(request):
    if request.method == "POST":
        event_participant = ParticipantModelForm(request.POST)
        if event_participant.is_valid():
            participant = event_participant.save()
            selected_events = event_participant.cleaned_data['event']
            participant.event.set(selected_events)  
            return render(request, 'dashboard/create_participant.html', {"event_participant": event_participant, "message": "added successfully"})
    else:
        event_participant = ParticipantModelForm()

    return render(request, 'dashboard/create_participant.html', {"event_participant": event_participant})

# def create_participant(request):
    
#      event_participant = ParticipantModelForm()
#      if request.method == "POST":
     
#         event_participant =  ParticipantModelForm(request.POST)
#         if event_participant.is_valid():
#                 event_participant.save()
              
#                 return render(request,'dashboard/create_participant.html',{"event_participant":event_participant,"message": "added successfully"})  
    
#         else:
           
#             event_participant = ParticipantModelForm()


#      return render(request,'dashboard/create_participant.html',{"event_participant": event_participant})

def update_event(request,id):
     event = Event.objects.get(id=id)
     event_e = EventModelForm(instance=event)
     if request.method == "POST":
        event_e  = EventModelForm(request.POST,instance=event)
        if event_e.is_valid():
                event_e.save()
                return redirect(reverse('update-event', args=[id]),{"message": "updated successfully"})
        
            
     return render(request,'dashboard/create_event.html',{"event_e": event_e})
     


def update_category(request,id):
     category = Category.objects.get(id=id)
     event_form = CategoryModelForm(instance=category)
     if request.method == "POST":
        event_form = CategoryModelForm(request.POST,instance = category)
        if event_form.is_valid():
                event_form.save()
               
                return redirect(reverse('dashboard'))
   
    

     return render(request,'dashboard/create_category.html',{"event_form": event_form})
     

def update_participant(request,id):
     event = Participant.objects.get(id=id)
     event_participant = ParticipantModelForm(instance=event)
     if request.method == "POST":
     
        event_participant =  ParticipantModelForm(request.POST,instance=event)
        if event_participant.is_valid():
                event_participant.save()
              
                return redirect(reverse('dashboard'))  
    
     return render(request,'dashboard/create_participant.html',{"event_participant": event_participant})


def detail_page(request,id):
     event = Event.objects.get(id=id)

     return render(request,'detail_page.html',{'event':event})
def delete_event(request,id):
    if request.method == 'POST':
      event = Event.objects.get(id=id)
      event.delete()
      return redirect('dashboard')
    else:
      return redirect('dashboard')
    
def home(request):
    search_query = request.GET.get('q', '').strip()  
    

    if search_query:
        events = Event.objects.filter(name__icontains=search_query)
    else:
        events = Event.objects.all()  

    context = {
        'events': events,
        'search_query': search_query,  
    }
    return render(request, 'home.html', context)
