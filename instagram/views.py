from django.shortcuts import render

def welcome(request):
    title = 'welcome'   
    return render(request,'instagram/home.html', {'title': title})
