from django.urls import path
from .views import donation_list

urlpatterns = [
    path('', donation_list, name='donate'),
]