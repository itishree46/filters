from django.shortcuts import render

# Create your views here.
def filter(request):
    d={'topic':'helLo tHis is Filter mETHod','p':3}
    return render(request,'filter.html',d)