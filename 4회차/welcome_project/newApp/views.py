from django.shortcuts import render

# Create your views here.
def hello(request) :
    userName = request.GET['name']
    return render(request, 'hello.html', {'userName' : userName})   

def welcome(request) :
    return render(request, 'welcome.html')

def template(request) :
    return render(request, 'template.html')