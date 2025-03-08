from django.urls import path
from users.views import register,sign_in,sign_out,admin_dashboard,assign_role,create_group,view_group,activate_user
urlpatterns = [
   path('register/',register,name='register'),
   path('sign-in/',sign_in,name='sign-in'),
   path('sign-out/',sign_out,name='sign-out'),
   path('admin-dashboard/',admin_dashboard,name='admin-dashboard'),
   path('activate/<int:user_id>/<str:token>/', activate_user,name='activate-user'),
   path('admin/<int:user_id>/assign-role/',assign_role,name='assign-role'),
   path('admin/create-group/',create_group,name='create-group'),
   path('admin/view-group/',view_group,name='view-group'),
   
]