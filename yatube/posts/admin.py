from django.contrib import admin
from .models import Post, Group


# Настройка админки для постов
class PostAdmin(admin.ModelAdmin):
    # Перечисляем поля, которые должны отображаться в админке
    list_display = (
        'pk',
        'text',
        'pub_date',
        'author',
        'group'
    )
    # Добавляем изменяемое поле со списком групп
    list_editable = ('group',)
    # Добавляем интерфейс для поиска по тексту постов
    search_fields = ('text',)
    # Добавляем возможность фильтрации по дате
    list_filter = ('pub_date',)
    # Это свойство сработает для всех колонок: где пусто — там будет эта строка
    empty_value_display = '-пусто-'


# Настройка админки для групп
class GroupAdmin(admin.ModelAdmin):
    # Автозаполнение поля slug при вводе title группы
    prepopulated_fields = {'slug': ('title',)}


# Регистрация моделей Post и Group
admin.site.register(Post, PostAdmin)
admin.site.register(Group, GroupAdmin)