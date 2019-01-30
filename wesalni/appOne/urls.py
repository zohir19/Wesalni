from django.urls import path
from appOne import views

urlpatterns = [
    path('',views.home_page,name='home'),
    path('contact/',views.contact_page,name="contact"),
    path('about/',views.about_page,name='about'),
]
