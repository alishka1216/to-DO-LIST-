from django.contrib import admin
from webapp.models import Article

# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'date']
    list_filter = ['date']
    search_fields = ['title', 'status']
    fields = ['id', 'title', 'date', 'status']
    readonly_fields = ['id']


admin.site.register(Article, ArticleAdmin)