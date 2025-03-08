from django.urls import path
from events.views import all_event,all_category,dashboard,event_detail,participant_dashboard,rsvp_event,organizer_dashboard, create_event, create_category, update_event, update_category, detail_page, delete_event, event_details, update_participant, activate_user, add_participant,participant_page,user_registered_events

urlpatterns = [
    path('organizer-dashboard/', organizer_dashboard, name='organizer-dashboard'),
    path('create-event/', create_event, name='create-event'),
    path('create-category/', create_category, name='create-category'),
    path('add-participant/', add_participant, name='add-participant'),
    path('update-participant/<int:user_id>/', update_participant, name='update-participant'),
    path('update-event/<int:id>/', update_event, name='update-event'),
    path('update-category/<int:id>/', update_category, name='update-category'),
    path('update-participant/<int:id>/', update_participant, name='update-participant'),
    path('detail_page/<int:id>/', detail_page, name='detail-page'),
    path('delete-event/<int:id>/', delete_event, name='delete-event'),
    path('event-details/', event_details, name='event-details'),
    path("users/activate/<str:user_id>/<str:token>/", activate_user, name="activate-user"),
    # path('participant-dashboard/',participant_event,name="participant-dashboard") ,
    # path('show-participant/',show_participant,name='show-participant'),
    path('events/<int:event_id>/participants/',participant_page, name='participant-page'),
    path('rsvp/<int:event_id>/', rsvp_event, name='rsvp-event'),
    path('activate/<int:user_id>/<str:token>/',activate_user, name='activate-user'),
    # path('events/<int:id>/', see_register_events, name='see_register_events'),
    path('user-registered-events/', user_registered_events, name='user-registered-events'),
    path('participant-dashboard/', participant_dashboard, name="participant-dashboard"),
    path('event/<int:event_id>/detail/',event_detail,name='event-detail'),
    path('dashboard/', dashboard, name='dashboard'),
    path('all-category/',all_category,name='all-category'),
    path('all-event/',all_event,name='all-event'),
]

