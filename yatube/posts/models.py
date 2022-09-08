from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


# Модель для групп
class Group(models.Model):
    title = models.CharField(max_length=200)  # Название группы
    slug = models.SlugField(unique=True)  # Адрес группы
    description = models.TextField()  # Описание группы

    # Метод возвращает имя сообщества
    def __str__(self):
        return self.title


# Модель для постов
class Post(models.Model):
    text = models.TextField()  # Текст поста
    pub_date = models.DateTimeField(auto_now_add=True)  # Дата публикации поста
    author = models.ForeignKey(  # Автор поста
        User,
        on_delete=models.CASCADE,
        related_name='posts'
    )
    group = models.ForeignKey(  # Группа для поста (опционально)
        Group,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='posts'
    )

    # Сортировка по дате публикации объектов Post
    class Meta:
        ordering = ['-pub_date']

    # Метод возвращает текст поста
    def __str__(self):
        return self.text
