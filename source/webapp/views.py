from django.shortcuts import render, get_object_or_404, redirect
from webapp.models import Article, STATUS_CHOICES

from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.urls import reverse
from webapp.forms import ArticleForm


def index_view(request):
    """
    Представление для отображения списка статей
    """
    articles = Article.objects.all()  # Получаем список статей из базы данных
    return render(request, 'index.html', context={
        'articles': articles})  # Возвращаем "скомпилированный" шаблон с использованием переданного списка статей


def article_view(request, pk):
    """
    Представление для отображение одной статьи
    """
    article = get_object_or_404(Article, id=pk)
    return render(request, 'article_view.html', context={'article': article})


def article_create_view(request):
    """
    Представление для создания статьи
    """
    if request.method == "GET":  # Если метод запроса GET - будет отображена форма создания статьи
        form = ArticleForm()
        return render(request, 'article_create.html', context={'form': form})
    elif request.method == "POST":  # Если метод запроса POST - будет отображён шаблон просмотра деталей статьи
        form = ArticleForm(data=request.POST)
        if form.is_valid():
            article = Article.objects.create(
                title=form.cleaned_data.get('title'),
                status=form.cleaned_data.get('status'),
                detailed_description=form.cleaned_data.get('detailed_description'),
                date=form.cleaned_data.get('date')
            )
            article.save()

        else:
            return render(request, 'article_create.html', context={'form': form})

        return redirect('article-view', pk=article.id)


def article_update_view(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'GET':
        form = ArticleForm(initial={
            'title': article.title,
            'detail_description': article.detailed_description,
            'status': article.status,
            'date': article.date
        })
        return render(request, 'article_update.html', context={'form': form, 'article': article})
    elif request.method == 'POST':
        form = ArticleForm(data=request.POST)
        if form.is_valid():
            article.title = form.cleaned_data['title']
            article.detailed_description = form.cleaned_data['detail_description']
            article.status = form.cleaned_data['status']
            article.date = form.cleaned_data['date']
            article.save()
            return redirect('article_view', pk=article.pk)
        else:
            return render(request, 'update.html', context={'form': form, 'article': article})


def article_delete_view(request, pk):
    article = get_object_or_404(Article, id=pk)
    if request.method == 'GET':
        return render(request, 'article_delete.html', context={'article': article})
    elif request.method == 'POST':
        article.delete()
    return redirect('article-list')
