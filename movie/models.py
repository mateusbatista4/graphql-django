from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Movie(models.Model):
    
    name = models.CharField(max_length=60)
    director = models.CharField(max_length=60)
    release_year = models.DateField()
    
    category = models.ForeignKey(Category, related_name="movies",on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name