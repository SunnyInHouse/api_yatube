from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Post(models.Model):
    text = models.TextField(
        'Текст поста',
    )
    pub_date = models.DateTimeField(
        'Дата публикации',
        auto_now_add=True,
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name='Автор поста',
    )
    image = models.ImageField(
        'Изображение к посту',
        upload_to='posts/',
        null=True,
        blank=True,
    )
    group = models.ForeignKey(
        'Group',
        on_delete=models.SET_NULL,
        related_name='posts',
        verbose_name='Сообщество для поста',
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.text[:15]

    class Meta:
        ordering = ['-pub_date', 'author']
        get_latest_by = '-published'


class Comment(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Автор комментария',
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Ссылка на пост',
    )
    text = models.TextField(
        'Текст комментария',
    )
    created = models.DateTimeField(
        'Дата добавления',
        auto_now_add=True,
        db_index=True,
    )

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f'Comment {self.author}: {self.text[:15]}'


class Group(models.Model):
    title = models.CharField(
        'Название сообщества',
        max_length=200,
    )
    slug = models.SlugField(
        'Имя URL для сообщества',
        unique=True,
    )
    description = models.TextField(
        'Описание сообщества',
        max_length=200,
    )

    def __str__(self):
        return self.title


class Follow(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='followers',
        verbose_name='Пользователь-подписчик',
    )
    following = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='followings',
        verbose_name='Пользователь, на которого подписываются',
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'following'],
                name='unique_user_following'
            )
        ]

    def __str__(self):
        return f'{self.user.username} follow to {self.author.username}'
