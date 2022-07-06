from django.shortcuts import render

# Create your views here.
def tele(request):
    return render(request, 'home/base.html')
