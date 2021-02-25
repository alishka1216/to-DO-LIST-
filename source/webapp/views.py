from django.shortcuts import render

from webapp.models import Article, STATUS_CHOICES


def index_view(request):
    """
    Представление для отображения списка статей
    """
    articles = Article.objects.all()  # Получаем список статей из базы данных
    return render(request, 'index.html', context={'articles': articles})  # Возвращаем "скомпилированный" шаблон с использованием переданного списка статей


def article_view(request):
    """
    Представление для отображение одной статьи
    """
    article_id = request.GET.get('id')
    article = Article.objects.get(id=article_id)
    return render(request, 'article_view.html', context={'article': article})


def article_create_view(request):
    """
    Представление для создания статьи
    """
    if request.method == "GET":  # Если метод запроса GET - будет отображена форма создания статьи
        return render(request, 'article_create.html', context={'choices': STATUS_CHOICES})
    elif request.method == "POST":  # Если метод запроса POST - будет отображён шаблон просмотра деталей статьи
        title = request.POST.get("title")
        status = request.POST.get("status")
        date = request.POST.get("date")

        article = Article.objects.create(
            title=title,
            status=status,
            date=date
        )

        return render(request, 'article_view.html', context={'article': article})
