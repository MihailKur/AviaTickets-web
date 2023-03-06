from django.shortcuts import render

def index(response):
    return render(response, 'main/index.html')

def aboutUs(response):
    return render(response, 'main/about.html')
