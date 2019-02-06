from django.shortcuts import render, redirect
from .forms import ContactForm, LoginForm, RegisterForm
from django.contrib.auth import authenticate, login


# Create your views here.

def home_page(request):
    contexte = {
        'title': 'Home page',
        'content': 'Welcome to the home page',
        'client': 'Welcome back to the home page'
    }
    return render(request, 'appOne/home.html', contexte)


def about_page(request):
    contexte = {
        'title': 'About page',
        'content': 'Welcome to the about page',
        'client': 'Welcome back to the about page'
    }
    return render(request, 'appOne/about.html', contexte)


def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    contexte = {
        "title": "Contact-Us",
        "content": "Welcome to the contact page",
        "form": contact_form,
        'client': 'Welcome back to the contact page'
    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)

    return render(request, 'appOne/contact.html', contexte)


def login_page(request):
    form = LoginForm(request.POST or None)
    contexte = {
        "title": "Login or Register",
        "form": form
    }
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None and password is not None:
            login(request, user)
            return redirect('/')
        else:
            contexte["error"] = True
            print("ERROR")
    return render(request, "appOne/login.html", contexte)


def register_page(request):

    contexte = {"title": "Register"}

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            email = form.cleaned_data.get("email")
            email_con = form.cleaned_data.get("email_con")
            password = form.cleaned_data.get("password")
            birth_date=form.cleaned_data.get("date_of_birth")
            phone=form.cleaned_data.get("phone")
            #city=form.cleaned_data.get("city")
            if email != email_con:
                contexte["error"] = True
            form.save()
            user = authenticate(username=username, password=password)
            login_page(request, user)
            return redirect('/')
    else:
        form = RegisterForm()

    contexte["form"] = form
    return render(request, "appOne/register.html", contexte)


def terms_page(request):
    contexte = {
        'title': 'Terms & conditions page',
        'content': 'Welcome to the Terms & conditions page',
    }
    return render(request, 'appOne/terms.html', contexte)


def account_page(request):
    contexte = {
        'title': 'My Account page',
        'content': 'Welcome to your Account page',
    }
    return render(request, 'appOne/account.html', contexte)
from django.contrib.auth import logout

def logout_page(request):
    logout(request)
    return render(request,'appOne/logout.html')
