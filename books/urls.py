from django.urls import path
from . import views


urlpatterns = [
    path('cre_books/',views.CreBook,name = 'cre_book'),
    path('books_list/<int:id>/update/',views.BookUpdate,name='book_update'),
    path('books_list/<int:id>/delete/',views.BookDel,name='delete'),
    path('',views.BooksList,name = 'book_list'),
    path('books_list/<int:id>/',views.BooksDetail, name = 'book_detail'),























    path('news_list', views.newsPostView, name='news_list'),
    path('news_list/<int:id>/', views.newsPostDetailView, name='news_detail'),


    
    path('time/',views.CurrentTimeView,name='current_time'),
    path('writers/',views.WritersView,name='writerss'),
    path('quotes/',views.QuotesView,name='quoteses'),


]