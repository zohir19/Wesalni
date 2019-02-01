from django.urls import path
from appOne import views

urlpatterns = [
    path('',views.home_page,name='home'),
    path('contact/',views.contact_page,name="contact"),
    path('about/',views.about_page,name='about'),
    path('login/',views.login_page,name='login'),
    path('register/',views.register_page,name='register'),
    path('terms/',views.terms_page,name='terms'),
    path('account/',views.account_page,name='account'),
]
