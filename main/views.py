from django.shortcuts import render

def index(request):
    return render(request, 'main/index.html',{})

def contact(request):
    return render(request, 'main/contact.html',{})


def services(request):
    return render(request, 'main/services.html',{})


def about_us(request):
    return render(request, 'main/about.html',{})

def works(request):
    return render(request, 'main/works.html',{})