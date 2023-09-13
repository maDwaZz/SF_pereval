from django.contrib.auth.models import User
from django.db import models


class PerevalAdded(models.Model):
    status_choices = [
        ('new', 'Новое'),
        ('pending', 'Ожидает подтверждения'),
        ('accepted', 'Подтверждено'),
        ('rejected', 'Отказано')]

    beauty_title = models.CharField(max_length=10, blank=True)
    title = models.CharField(max_length=255)
    other_titles = models.CharField(max_length=255, blank=True)
    connect = models.TextField(blank=True)
    add_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    coords = models.ForeignKey('Coords', on_delete=models.CASCADE)
    level_winter = models.CharField(max_length=10, blank=True)
    level_spring = models.CharField(max_length=10, blank=True)
    level_summer = models.CharField(max_length=10, blank=True)
    level_autumn = models.CharField(max_length=10, blank=True)
    status = models.CharField(choices=status_choices, default='new')

    def __str__(self):
        if self.beauty_title:
            return f'{self.beauty_title} {self.title}'
        else:
            return self.title

    class Meta:
        db_table = 'pereval_added'


class Coords(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    height = models.IntegerField()

    def __str__(self):
        return f'ID координат: {str(self.id)}'

    class Meta:
        db_table = 'pereval_coords'
    

class PerevalImages(models.Model):
    pereval = models.ForeignKey(PerevalAdded, on_delete=models.CASCADE)

    def __str__(self):
        return f'ID фото: {str(self.id)}'

    class Meta:
        db_table = 'pereval_images'
