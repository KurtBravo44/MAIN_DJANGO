from django.db import models

NULLABLE = {'null':True, 'blank':True}


class Client(models.Model):
    first_name = models.CharField(max_length=25, verbose_name='имя')
    middle_name = models.CharField(max_length=25, verbose_name='отчество')
    last_name = models.CharField(max_length=25, verbose_name='фамилия')
    email = models.EmailField(max_length=100, verbose_name='почта')
    message = models.TextField(verbose_name='сообщение', **NULLABLE)

    def __str__(self):
        return f'Клиент: {self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
