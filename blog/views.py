from django.shortcuts import render

def login_view(request):
    return render(request, "blog/login.html")
