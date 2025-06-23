from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,'home.html')

def view(request):
    return render(request,'emoji.html',{'content':"Feeling Emoji-tional? Select Emoji!"})

def emoji(request):
    if 'b1' in request.POST:
        return render(request,'e1.html',{'name':'e11'})
    if 'b2' in request.POST:
        return render(request,'e1.html',{'name':'e2'})
    if 'b3' in request.POST:
        return render(request,'e1.html',{'name':'e3'})
    if 'b4' in request.POST:
        return render(request,'e1.html',{'name':'e4'})
    if 'b5' in request.POST:
        return render(request,'e1.html',{'name':'e5'})
    if 'b6' in request.POST:
        return render(request,'e1.html',{'name':'e6'})
    if 'b7' in request.POST:
        return render(request,'e1.html',{'name':'e7'})
    if 'b8' in request.POST:
        return render(request,'e1.html',{'name':'e8'})
    if 'b9' in request.POST:
        return render(request,'e1.html',{'name':'e12'})
    if 'b10' in request.POST:
        return render(request,'e1.html',{'name':'e10'})
    
def home1(request):
        return render(request,'home.html')