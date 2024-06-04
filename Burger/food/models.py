from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class FoodType(models.Model):
    nomi = models.CharField(max_length=50)

    def __str__(self):
        return self.nomi

class Food(models.Model):
    food_type = models.ForeignKey(FoodType, on_delete=models.CASCADE)
    nomi = models.CharField(max_length=50)
    tarkibi = models.TextField()
    narxi = models.IntegerField()

    def __str__(self):
        return self.nomi

class Comment(models.Model):
    text = models.TextField()
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

