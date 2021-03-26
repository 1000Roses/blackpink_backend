from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Song(models.Model):
    name = models.CharField(max_length=50)
    release_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name

class Prize(models.Model):
    name = models.CharField(max_length=150)
    song = models.ForeignKey(Song, on_delete=models.CASCADE,related_name='prize', null=True,blank=True )

    def __str__(self):
        return self.name

class Member(models.Model):
    name        = models.CharField(max_length = 50)
    age         = models.IntegerField(validators=[MinValueValidator(0),
                                       MaxValueValidator(100)])
    song        = models.ManyToManyField(Song)
    description = models.TextField()

    def __str__(self):
        return self.name
