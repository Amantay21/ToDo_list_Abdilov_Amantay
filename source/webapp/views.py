from django.shortcuts import render
from webapp.models import Article
from django.http import HttpResponseRedirect


def index_view(request):
    articles = Article.objects.all()
    return render(request, 'index.html', {'articles': articles})


def article_view(request):
    article_id = request.GET.get('id')
    article = Article.objects.get(id=article_id)
    return render(request, 'article_view.html', {'article': article})


def article_create_view(request):
    if request.method == "GET":
        return render(request, 'article_create.html')
    elif request.method == "POST":
        Article.objects.create(
            title=request.POST.get('title'),
            content=request.POST.get('content'),
            author=request.POST.get('author')
        )
        return HttpResponseRedirect('/')
