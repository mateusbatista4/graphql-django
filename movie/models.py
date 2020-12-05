from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Movie(models.Model):
    SAMPLE_LANGUAGES = (
        ('Ingles', 'en'),
        ('Portugues', 'pt'),
        ('Espanhol', 'es'),
    )
    name = models.CharField(max_length=60)
    director = models.CharField(max_length=60)
    release_year = models.DateField()
    languages =  models.CharField(choices=SAMPLE_LANGUAGES, max_length=20),
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name