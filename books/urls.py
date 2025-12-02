from django.urls import path
from . import views


urlpatterns = [
    path('', views.newsPostView, name='home'),  # главная: список
    path('news_list/', views.newsPostView, name='news_list'),
    path('news_list/<int:id>/', views.newsPostDetailView, name='news_detail'),
    path('time',views.CurrentTimeView,name='current_time'),
    path('writers',views.WritersView,name='writerss'),
    path('quotes',views.QuotesView,name='quoteses')
]