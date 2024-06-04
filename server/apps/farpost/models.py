from django.db import models


class Advert(models.Model):
    """Модель объявления"""
    # ID переопределен, чтобы можно было сделать его таким, как на сайте
    id = models.PositiveIntegerField(
        primary_key=True,
    )
    title = models.CharField(
        verbose_name='заголовок',
        max_length=200,
    )
    author = models.CharField(
        verbose_name='автор',
        max_length=200,
    )
    views = models.PositiveIntegerField(
        verbose_name='кол-во просмотров',
        default=0,
    )
    position = models.PositiveIntegerField(
        verbose_name='позиция в списке',
        default=0,
    )

    def __str__(self):
        return f'{self.title}, {self.author}'

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'
