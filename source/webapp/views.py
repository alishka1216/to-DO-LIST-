from django.shortcuts import render, get_object_or_404, redirect
from webapp.models import Article, STATUS_CHOICES


from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.urls import reverse


def index_view(request):
    """
    Представление для отображения списка статей
    """
    articles = Article.objects.all()  # Получаем список статей из базы данных
    return render(request, 'index.html', context={'articles': articles})  # Возвращаем "скомпилированный" шаблон с использованием переданного списка статей


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
        return render(request, 'article_create.html', context={'choices': STATUS_CHOICES})
    elif request.method == "POST":  # Если метод запроса POST - будет отображён шаблон просмотра деталей статьи
        title = request.POST.get("title")
        detailed_description = request.POST.get("detail_discrb")
        status = request.POST.get("status")
        date = request.POST.get("date")
        if not date:
            date=None
        if not detailed_description:
            detailed_description=None
        if not title:
            title=None

        article = Article.objects.create(
            title=title,
            status=status,
            detailed_description=detailed_description,
            date=date

        )

        return redirect('article-view', pk=article.id)