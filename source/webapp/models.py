from django.db import models


# Create your models here.
STATUS_CHOICES = [('new', 'Новая'), ('in_progress', 'В процессе'),  ('done', 'Сделано')]
class Article(models.Model):
    title = models.CharField(max_length=3000, null=False, blank=False)
    detailed_description = models.CharField(max_length=3000, null=True, blank=True)
    status = models.CharField(max_length=200, null=True, blank=True, choices=STATUS_CHOICES, default='new')
    date = models.DateField(null=True, blank=True)

    class Meta:
        db_table = 'articles'
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'

