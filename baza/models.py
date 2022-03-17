from django.db import models


class Reader(models.Model):
    fio = models.CharField(max_length=255, verbose_name='Фио читателя')
    eticket = models.CharField(max_length=13, blank=True, verbose_name='Читательский билет')
    phone = models.CharField(max_length=18, blank=True, verbose_name='Телефон')

    class Meta:
        verbose_name = 'Читатель'
        verbose_name_plural = 'Читатели'

    def __str__(self):
        return self.fio



