from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_news, name='news'),
    path('/<int:pk>', views.NewsDetailView.as_view(), name='news_detail'),
    path('/add', views.NewsCrateView.as_view(), name='add_news'),
    path('/<int:pk>/redact', views.NewsUpdateView.as_view(), name='redact_new'),
    path('/<int:pk>/delete', views.NewsDeleteView.as_view(), name='delete_new'),
]
