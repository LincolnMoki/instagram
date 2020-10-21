from django.urls import path
from . import views

urlpatterns = [
    path('',views.welcome, name='home'),
    path('',views.post_details, name='post_details')
]    