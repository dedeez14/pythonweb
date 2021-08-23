from django.db import models

# Create your models here.
class meetup(models.Model):
    username = models.CharField(max_length=25)
    slug = models.SlugField(unique=True, null=True)
    genreKonten = models.CharField(max_length=50)
    judulKonten = models.CharField(max_length=150)
    

    def __str__(self):
        return self.username