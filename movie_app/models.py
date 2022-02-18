from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Movie(models.Model):
    name = models.CharField(max_length=40)
    rating = models.IntegerField()
    year = models.IntegerField(default=1999)
    budget = models.IntegerField(default=1000000)
    slug = models.SlugField(default='', max_length=10, null=False, db_index=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Movie, self).save()


    def get_url(self):
        return reverse('movie-detail', args=[self.slug])

    def __str__(self):
        return f'{self.name} - {self.year}г. {self.budget}$ {self.rating}%'