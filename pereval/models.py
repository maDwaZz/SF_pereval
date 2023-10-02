from django.contrib.auth.models import User
from django.db import models


class PerevalUser(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    sur_name = models.CharField(max_length=50, verbose_name='Отчество', blank=True)
    email = models.EmailField(blank=False, unique=True, verbose_name='Электронная почта')
    phone = models.CharField(max_length=50, verbose_name='Телефон', blank=True)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class PerevalAdded(models.Model):
    status_choices = [
        ('new', 'Новая запись'),
        ('pending', 'Ожидает подтверждения'),
        ('accepted', 'Подтверждено'),
        ('rejected', 'Отказано')]

    beauty_title = models.CharField(max_length=10, blank=True, verbose_name='Вид объекта')
    title = models.CharField(max_length=255, verbose_name='Наименование')
    other_titles = models.CharField(max_length=255, blank=True, verbose_name='Прочие наименования')
    connect = models.TextField(blank=True, verbose_name='Соединение')
    add_time = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    user = models.ForeignKey(PerevalUser, on_delete=models.CASCADE, verbose_name='Пользователь')
    coords = models.ForeignKey('Coords', on_delete=models.CASCADE, verbose_name='Координаты')
    level_winter = models.CharField(max_length=10, blank=True, verbose_name='Сложность - Зима')
    level_spring = models.CharField(max_length=10, blank=True, verbose_name='Сложность - Весна')
    level_summer = models.CharField(max_length=10, blank=True, verbose_name='Сложность - Лето')
    level_autumn = models.CharField(max_length=10, blank=True, verbose_name='Сложность - Осень')
    status = models.CharField(choices=status_choices, default='new', verbose_name='Статус проверки записи')

    def __str__(self):
        if self.beauty_title:
            return f'{self.id} {self.beauty_title} {self.title}'
        else:
            return self.title

    class Meta:
        db_table = 'pereval_added'
        verbose_name = 'Объект'
        verbose_name_plural = 'Объекты'


class Coords(models.Model):
    latitude = models.FloatField(verbose_name='Широта')
    longitude = models.FloatField(verbose_name='Долгота')
    height = models.IntegerField(verbose_name='Высота')

    def __str__(self):
        return f'ID координат: {str(self.id)}'

    class Meta:
        db_table = 'pereval_coords'
        verbose_name = 'Координаты'
        verbose_name_plural = 'Координаты'
    

class PerevalImages(models.Model):
    pereval = models.ForeignKey(PerevalAdded, blank=True, on_delete=models.CASCADE, verbose_name='Объект', related_name='images')
    data = models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/', verbose_name='Фото')
    title = models.CharField(max_length=255, blank=True, verbose_name='Название')

    def __str__(self):
        return f'{str(self.id)} {self.title}'

    class Meta:
        db_table = 'pereval_images'
        verbose_name = 'Фото'
        verbose_name_plural = 'Фото'
