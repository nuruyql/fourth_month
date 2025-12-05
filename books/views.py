from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from datetime import datetime
from .models import AboutYou




def newsPostView(request):
    if request.method == 'GET':
        posts = AboutYou.objects.all().order_by('-created_at')
        return render(
            request,
            'books/news_list.html',
            {'posts': posts}
        )

def newsPostDetailView(request, id):
    if request.method == 'GET':
        post = get_object_or_404(AboutYou, id=id)
        return render(
            request,
            'books/news_detail.html',
            {'post': post}
        )

def WritersView(request):
    if request.method == 'GET':
        return HttpResponse(
            "Leo Tolstoy, William Shakespeare, George Orwell, Mark Twain, "
            "Jane Austen, Ernest Hemingway, Agatha Christie, J.K. Rowling, "
            "Gabriel García Márquez, Fyodor Dostoevsky"
        )

def QuotesView(request):
    quotes = [
        "“To be, or not to be, that is the question.” – William Shakespeare",
        "“All we have to decide is what to do with the time that is given us.” – J.R.R. Tolkien",
        "“In the middle of difficulty lies opportunity.” – Albert Einstein",
        "“Not all those who wander are lost.” – J.R.R. Tolkien",
        "“The only way to do great work is to love what you do.” – Steve Jobs",
    ]
    html = "<h1>5 quoteses of famous people</h1><ul>"
    for q in quotes:
        html += f"<li>{q}</li>"
    html += '</ul>'
    return HttpResponse(html)

def CurrentTimeView(request):
    current_time = datetime.now()
    if request.method == 'GET':
        return HttpResponse(f'Current time is {current_time}')