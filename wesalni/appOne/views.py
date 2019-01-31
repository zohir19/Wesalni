from django.shortcuts import render,redirect
from appOne.forms import ContactForm,LoginForm,RegisterForm
from django.contrib.auth import authenticate,login,get_user_model
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
def login_page(request):
    form= LoginForm(request.POST or None)
    contexte={
        "form":form
    }
    print("User logged in")
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request,username=username,password=password)
        print(user)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            print("ERROR")
    return render(request,"appOne/login.html",contexte)
User= get_user_model()      
def register_page(request):
    form= RegisterForm(request.POST or None)
    contexte={
        "form":form
    }
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        email=form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        new_user=User.objects.create_user(username,email,password)
        print(new_user)
    return render(request,"appOne/register.html",contexte)
    
def terms_page(request):
    contexte={
        'title':'Terms & conditions page',
        'content':'Welcome to the Terms & conditions page',   
    }
    return render(request,'appOne/terms.html',contexte)
   

    
