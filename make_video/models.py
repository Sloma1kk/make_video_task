from django.db import models


class UserRequest(models.Model):
    text = models.CharField(max_length=1024, verbose_name='Текст')
    date = models.DateField(auto_now_add=True, verbose_name='Дата запроса')

    class Meta:
        verbose_name = 'Запрос пользователя'
        verbose_name_plural = 'Запросы пользователей'

    def __str__(self):
        return self.text
