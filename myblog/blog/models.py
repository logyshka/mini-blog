from django.db import models


class Publication(models.Model):
    """Данные о публикации"""

    class Meta:
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'

    title = models.CharField(
        max_length=200,
        verbose_name='Заголовок публикации'
    )
    content = models.TextField(
        verbose_name='Текст публикации'
    )
    author = models.CharField(
        max_length=100,
        verbose_name='Автор публикации'
    )
    published_at = models.DateTimeField(
        null=True,
        default=None,
        verbose_name='Дата публикации'
    )
    image = models.ImageField(
        upload_to='images/%Y/%m/%d/',
        verbose_name='Изображение'
    )

    def __str__(self) -> str:
        return f'{self.title} | {self.author}'


class Comment(models.Model):
    """Данные о комментарии"""

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    email = models.EmailField(
        verbose_name='Email отправителя'
    )
    username = models.CharField(
        max_length=100,
        verbose_name='Имя отправителя'
    )
    comment = models.TextField(
        verbose_name='Текст комментария',
        max_length=2000
    )
    publication = models.ForeignKey(
        Publication,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Публикация'
    )

    def __str__(self) -> str:
        return f'{self.username} | {self.comment}'


class Like(models.Model):
    """Данные о лайках"""
    class Meta:
        verbose_name = 'Лайк'
        verbose_name_plural = 'Лайки'

    ip = models.CharField(
        max_length=100,
        verbose_name='IP'
    )
    publication = models.ForeignKey(
        Publication,
        on_delete=models.CASCADE,
        related_name='likes',
        verbose_name='Публикация'
    )

    def __str__(self) -> str:
        return f'{self.ip} | {self.publication}'
