from django.shortcuts import render

# Create your views here.


def Level1(request):
    return render(request,'level/index.html')


def Level2(request):
    return render(request,'index.html')