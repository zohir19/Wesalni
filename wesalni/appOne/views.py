from django.shortcuts import render,redirect
from appOne.forms import ContactForm
# Create your views here.
def home_page(request):
    contexte={
        'title':'Home page',
        'content':'Welcome to the home page',
        'client':'Welcome back to the home page'
    }
    return render(request,'appOne/home.html',contexte)
def about_page(request):
    contexte={
        'title':'About page',
        'content':'Welcome to the about page',
        'client':'Welcome back to the about page'
    }
    return render(request,'appOne/about.html',contexte)
def contact_page(request):
    contact_form= ContactForm(request.POST or None)
    contexte={
        "title":"Contact-Us",
        "content":"Welcome to the contact page",
        "form":contact_form,
        'client':'Welcome back to the contact page'
    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)
    
    return render(request,'appOne/contact.html',contexte)
   

    
