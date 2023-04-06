from django.shortcuts import render

# Create your views here.
def a2_first(request):
    return render(request,'a2_first.html',{'name':'Rakesh'})

def a2_second(request):
    d={'a':2}
    return render(request,'a2_second.html',d)
