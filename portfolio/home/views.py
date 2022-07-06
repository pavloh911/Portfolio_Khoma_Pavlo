from django.shortcuts import render, redirect
from .forms import MessagesForUsForm
from .models import MessagesForUs
from news.models import News
from django.contrib import messages


# Create your views here.
# <!--{% extends 'home/base.html'%}-->

def home_page(request):
    if request.method == 'POST':
        form = MessagesForUsForm(request.POST)
        if form.is_valid():
            form.save()
            return messege(request, request.POST['user_name'], True)
        else:
            return messege(request, request.POST['user_name'], False)
    news = News.objects.all().order_by('-date')
    news = news[:3] if len(news) > 3 else news
    message_form = MessagesForUsForm(request.POST, request.FILES)
    info = {'message': message_form, 'news': news}
    return render(request, 'home/index.html', info)


def messege(request, name='', is_correct=False):
    if request.method == 'POST':
        if is_correct:
            info = {'name': name, 'text': 'we received your message, wait and we will contact you'}
        else:
            info = {'name': name, 'text': 'sorry, something went wrong, try again later'}
    else:
        info = {'name': '', 'text': 'you can send message for us on the home page'}
    return render(request, 'home/message.html', info)


def view_massages(request):
    if request.method == 'POST':
        if (status := request.POST['sort']) == 'new':
            messages = MessagesForUs.objects.filter(status=status).order_by('-data')
        elif (status := request.POST['sort']) == 'worked':
            messages = MessagesForUs.objects.filter(status=status).order_by('-data')
        else:
            status = 'all'
            messages = MessagesForUs.objects.all().order_by('-data')
    else:
        status = 'all'
        messages = MessagesForUs.objects.all().order_by('-data')
    return render(request, 'home/messanges_for_us.html', {'messages': messages, 'status': status})


def change_status(request):
    if request.method == 'POST':
        mes = MessagesForUs.objects.get(id=request.POST['id'])
        mes.status = 'new' if mes.status == 'worked' else 'worked'
        mes.save()
    return redirect('messages_for_us')

