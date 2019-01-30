from django.urls import path
from appOne import views

urlpatterns = [
    path('',views.home_page,name='home'),
]
