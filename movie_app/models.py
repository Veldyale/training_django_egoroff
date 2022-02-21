from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.core.validators import MaxValueValidator, MinValueValidator  # валидатор для значений


class Movie(models.Model):
    EUR = 'EUR'
    USD = 'USD'
    RUB = 'RUB'
    CURRENCY_CHOICES = [
        (EUR, 'Euro'),
        (USD, 'Dollars'),
        (RUB, 'Rubles')
    ]

    name = models.CharField(max_length=40)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])

    year = models.IntegerField(blank=True, validators=[MinValueValidator(1900)])
    budget = models.IntegerField(default=1000000, validators=[MinValueValidator(1)])

    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default=USD)
    slug = models.SlugField(default='', null=False, db_index=True)
    director = models.ForeignKey('Director', on_delete=models.CASCADE, null=True, blank=True)
    actors = models.ManyToManyField('Actor')

    def get_url(self):
        return reverse('movie-detail', args=[self.slug])

    def __str__(self):
        return f'{self.name} - {self.rating}%'


class Director(models.Model):
    full_name = models.CharField(max_length=100)

    def __str__(self):
        return self.full_name


class Actor(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    GENDERS = [
        (MALE, 'Мужчина'),
        (FEMALE, 'Женщина'),
    ]

    full_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDERS, default=MALE)

    def __str__(self):
        if self.gender == self.MALE:
            return f'Актер - {self.full_name}'
        else:
            return f'Актриса - {self.full_name}'
