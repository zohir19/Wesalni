from django.shortcuts import render

# Create your views here.

def profile(request):
    context = {
        "title" : "Profile"
    }
    return render(request, 'client/profile.html', context)
