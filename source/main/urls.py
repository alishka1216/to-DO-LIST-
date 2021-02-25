from django.contrib import admin
from django.urls import path

from webapp.views import index_view, article_view, article_create_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view),  # URL для отображения списка статей
    path('articles/add/', article_create_view),  # URL для создания статьи
    path('article/', article_view)  # URL для просмотра деталей статьи
]
