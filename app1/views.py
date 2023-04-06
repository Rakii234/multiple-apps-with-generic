from django.shortcuts import render

# Create your views here.
def a1_first(request):
    d={'a':2}
    return render(request,'a1_first.html',d)
def a1_second(request):
    d={'greeting':3}
    return render(request,'a1_second.html',d)