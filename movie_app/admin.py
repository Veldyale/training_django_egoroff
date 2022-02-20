from django.contrib import admin, messages
from django.db.models import QuerySet
from .models import *


# Register your models here.
class RatingFilter(admin.SimpleListFilter):
    title = 'по рейтингу'
    parameter_name = 'rating'

    def lookups(self, request, model_admin):
        return [
            ('выше 80', 'Топ'),
            ('от 60 до 80', 'Высокий'),
            ('от 40 до 59', 'Средний'),
            ('ниже 40', 'Низкий'),
        ]

    def queryset(self, request, queryset: QuerySet):
        if self.value() == 'ниже 40':
            return queryset.filter(rating__lt=40)
        if self.value() == 'от 40 до 59':
            return queryset.filter(rating__gte=40).filter(rating__lt=60)
        if self.value() == 'от 60 до 80':
            return queryset.filter(rating__gte=60).filter(rating__lte=80)
        if self.value() == 'выше 80':
            return queryset.filter(rating__gt=80)
        return queryset.all()


@admin.register(Movie)  # способ регистрайии №2
class MovieAdmin(admin.ModelAdmin):
    # fields = ['name', 'rating']  # необязательный атрибут, отображаемые поля
    # exclude = ['slug']  # необязательный атрибут, противоположный атридуту fields, поля которые нужно ислючить
    # readonly_fields = ['year']  # запрет на изменение выбранных полей
    prepopulated_fields = {'slug': ('name',)}  # вычисляемое поле, в данном случае сам пишет slug по имени
    list_display = ['name', 'rating', 'director', 'currency', 'budget', 'rating_status']
    list_editable = ['rating', 'currency', 'budget']
    list_filter = ['currency', 'director', RatingFilter]
    search_fields = ['name__istartswith', 'rating', 'currency',
                     'budget']  # __startswith - поиск сначала строки, __istartswith - убирает чувствительность к регистру
    ordering = ['name']
    list_per_page = 4
    actions = ['set_dollars', 'set_euros', 'set_rubles', 'set_rating']

    @admin.display(ordering='-rating',
                   description='Статус')  # сортировка для rating_status, затем добавили кастомный фильтр и теперь эта функция не актуальна
    def rating_status(self,
                      value: Movie):  # value - экземпляр класса Movie, запись ": Movie" не обязательная, но открывает доступ к подсвечиванию
        if value.rating < 50:
            return 'Низкий рейтинг'
        if value.rating < 70:
            return 'Средний рейтинг'
        if value.rating < 85:
            return 'Высокий рейтинг'
        return 'Топ'

    @admin.action(description='Установить валюту в доллары')  # Показываем django что мы функция является действием
    def set_dollars(self, request, qs: QuerySet):
        count_updated = qs.update(currency=Movie.USD)
        self.message_user(
            request,
            f'Было обновлено {count_updated} записей',
            messages.SUCCESS  # Задаем цвет и уровень сообщения
        )

    @admin.action(description='Установить валюту в евро')  # Показываем django что мы функция является действием
    def set_euros(self, request, qs: QuerySet):
        count_updated = qs.update(currency=Movie.EUR)
        self.message_user(
            request,
            f'Было обновлено {count_updated} записей',
            messages.WARNING  # Задаем цвет и уровень сообщения
        )

    @admin.action(description='Установить валюту в рублях')  # Показываем django что мы функция является действием
    def set_rubles(self, request, qs: QuerySet):
        count_updated = qs.update(currency=Movie.RUB)
        self.message_user(
            request,
            f'Было обновлено {count_updated} записей',
            messages.ERROR  # Задаем цвет и уровень сообщения

        )

    @admin.action(description='Обнулить рейтинг')  # Показываем django что мы функция является действием
    def set_rating(self, request, qs: QuerySet):
        qs.update(rating=1)


@admin.register(Director)  # способ регистрайии №2
class DirectorAdmin(admin.ModelAdmin):
    list_display = ['full_name']

# admin.site.register(Movie, MovieAdmin)  # способ регистрайии №1
