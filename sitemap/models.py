from django.db import models

# Create your models here.
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название Бассейна')  # Максимум 150 символов


class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название речного бассейна')  # Заголовок
    content = models.TextField(default='',
                               verbose_name='Текст')  # Описание
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name='Дата создания')  # Автоматически возьмет дату создания объекта
    updated_at = models.DateTimeField(auto_now=True,
                                      verbose_name='Дата обновления')  # Берет дату любого изменения в объекте
    photo = models.ImageField(upload_to='photos/', blank=True, null=True,
                              verbose_name='Изображение')  # blank=True - не обязательна для заполнения
    # null=True - может быть пустой в базе
    watched = models.IntegerField(default=0, verbose_name='Просмотры')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано ли')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    author = models.ForeignKey(User, default=None, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'О Бассейне'
        verbose_name_plural = 'Информация о речных бассейнах'


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text


class Search(models.Model):
    address = models.CharField(max_length=200, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address
