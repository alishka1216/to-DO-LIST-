from django.db import models


# Create your models here.
STATUS_CHOICES = [('new', 'Новая'), ('in_progress', 'В процессе'),  ('done', 'Сделано')]
class Article(models.Model):
    title = models.CharField(max_length=3000, null=False, blank=False)
    status = models.CharField(max_length=200, null=True, blank=True, choices=STATUS_CHOICES, default='new')
    date = models.DateField(null=True, blank=True)

    class Meta:
        db_table = 'articles'
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    # def __str__(self):
    #     return f'{self.id}. {self.author}: {self.title}'
