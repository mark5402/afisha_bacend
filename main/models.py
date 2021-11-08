

from django.db import models


# Create your models here.

class Cinema(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    genres = models.TextField(null=True, blank=True)
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE, null=True, blank=True)

    #
    def __str__(self):
        return self.title


class Review(models.Model):
    text = models.CharField(max_length=50)
    # movie = models.ManyToManyField(Movie, null=True)

    #
    def __str__(self):
        return self.text


class Genre(models.Model):
    name = models.CharField(max_length=50)

    #
    def __str__(self):
        return self.name
