from django.shortcuts import render

# Create your views here.
def home_page(request):
    contexte={
        'title':'Home page',
        'content':'Welcome to the home page',
        'client':'Welcome back to the home page'
    }
    return render(request,'appOne/home.html',contexte)