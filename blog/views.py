from django.shortcuts import render

def index_view(request):
    return render(request, "blog/login.html")

def login_view(request):
    return render(request, "blog/login.html")
