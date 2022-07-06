from django.shortcuts import render, redirect
from .forms import NewsForm
from .models import News, Group_of_news
from django.views.generic import DetailView, DeleteView, UpdateView, CreateView


# Create your views here.
class NewsDetailView(DetailView):
    model = News
    template_name = 'home/news_detail.html'
    context_object_name = 'new'


class NewsCrateView(CreateView):
    model = News
    template_name = 'home/add_news.html'
    # fields = ['title', 'full_text', 'img', 'author', 'author_img', 'group']
    form_class = NewsForm
    context_object_name = 'news'


class NewsUpdateView(UpdateView):
    model = News
    template_name = 'home/add_news.html'
    form_class = NewsForm
    context_object_name = 'news'


class NewsDeleteView(DeleteView):
    model = News
    success_url = '/news/'
    template_name = 'home/delete_news.html'
    context_object_name = 'news'


def show_news(request):
    news_groups = Group_of_news.objects.all()

    if request.method == 'POST':
        if 'group' in request.POST:
            group = request.POST['group']
            news = News.objects.filter(group=group).order_by('-date')
        else:
            group = 'all'
            news = News.objects.all().order_by('-date')
    else:
        group = 'all'
        news = News.objects.all().order_by('-date')

    info = {'news': news, 'group': group, 'news_groups': news_groups}
    return render(request, 'home/news.html', info)

