from django.shortcuts import render

# Create your views here.
def for_loop(request):
    d={'name':'Sreenivasulu','field':'IT'}
    return render(request,'for_loop.html',context=d)