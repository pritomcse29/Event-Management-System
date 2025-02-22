from django.urls import path
from events.views import dashboard,create_event,create_category,create_participant,update_event,update_category, update_participant,detail_page,delete_event,home
urlpatterns = [
    path('dashboard/',dashboard,name='dashboard'),
    path('create-event/',create_event,name='create-event'),
    path('create-category/',create_category,name='create-category'),
    path('create-participant/',create_participant,name='create-participant'),
    path('update-event/<int:id>/',update_event,name='update-event'),
    path('update-category/<int:id>/',update_category,name='update-category'),
    path('update-participant/<int:id>/',update_participant,name='update-participant'),
    path('detail_page/<int:id>/',detail_page,name='detail-page'),
    path('delete-event/<int:id>/',delete_event,name='delete-event'),
    path('home/',home,name='home')
]