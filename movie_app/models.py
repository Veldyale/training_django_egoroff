from django.db import models

class Movie(models.Model):
    name = models.CharField(max_length=40)
    rating = models.IntegerField()
    year = models.IntegerField(default=1900)
    budget = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.name} - {self.year}г. {self.budget}$ {self.rating}%'