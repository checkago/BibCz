from django.db import models


class Reader(models.Model):
    fio = models.CharField(max_length=255, verbose_name='Фио читателя', db_index=True)
    eticket = models.CharField(max_length=13, blank=True, verbose_name='Читательский билет', db_index=True)
    phone = models.CharField(max_length=18, blank=True, verbose_name='Телефон')
    comment = models.CharField(max_length=100, blank=True, verbose_name='Комментарий')

    class Meta:
        verbose_name = 'Читатель'
        verbose_name_plural = 'Читатели'

    def __str__(self):
        return self.fio



