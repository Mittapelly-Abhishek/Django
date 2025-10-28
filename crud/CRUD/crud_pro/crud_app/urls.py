from django.urls import path
from . import views

urlpatterns=[
    path("get_user/", views.get_user),    
    path("get_user/<int:user_id>",view=views.get_user),
    path("add_user/",view=views.add_user),
    path("update_user/<int:user_id>",view=views.update_user),
    path("update_user_put/<int:user_id>",view=views.update_user_put),
    path("delete_user/<int:user_id>",view=views.delete_user)
    
]