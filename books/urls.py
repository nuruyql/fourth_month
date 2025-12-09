from django.urls import path
from . import views


urlpatterns = [
    path('cre_books/',views.CreBook,name = 'cre_book'),
    path('books_list/',views.BooksList,name = 'book_list'),
    path('book_detail/',views.BooksDetail, name = 'book_detail'),

    path('', views.newsPostView, name='news_list'),
    path('news_list/<int:id>/', views.newsPostDetailView, name='news_detail'),


    
    path('time/',views.CurrentTimeView,name='current_time'),
    path('writers/',views.WritersView,name='writerss'),
    path('quotes/',views.QuotesView,name='quoteses'),


]