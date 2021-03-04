from django.contrib import admin
from django.urls import path

from webapp.views import (
    index_view,
    article_view,
    article_create_view,
    article_update_view,
    article_delete_view
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view, name='article-list'),  # URL для отображения списка статей
    path('articles/add/', article_create_view, name='article-add'),  # URL для создания статьи
    path('article/<int:pk>/', article_view, name='article-view'),  # URL для просмотра деталей статьи
    path('article/update/<int:pk>/', article_update_view, name='article-update'),
    path('article/delete/<int:pk>/', article_delete_view, name='article-delete')
]
