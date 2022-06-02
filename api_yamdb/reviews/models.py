import datetime as dt

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import AbstractUser


def current_year():
    return dt.date.today().year


class User(AbstractUser):
    USER, MODERATOR, ADMIN = 'user', 'moderator', 'admin'
    ROLES_CHOICES = [
        (USER, 'Пользователь'),
        (MODERATOR, 'Модератор'),
        (ADMIN, 'Админ'),
    ]

    username = models.CharField(
        max_length=150,
        unique=True
    )
    email = models.EmailField(
        max_length=254,
        unique=True
    )
    first_name = models.CharField(
        max_length=150,
        blank=True
    )
    last_name = models.CharField(
        max_length=150,
        blank=True
    )
    bio = models.TextField(
        'Биография',
        blank=True
    )
    role = models.CharField(
        max_length=16,
        choices=ROLES_CHOICES,
        default=USER
    )
    # Enum: "user" "moderator" "admin"
    # Администратор, модератор или пользователь. По умолчанию user.


class Category(models.Model):
    name = models.CharField(
        verbose_name='categories',
        max_length=200
    )
    slug = models.SlugField(
        max_length=100,
        unique=True,
        blank=True
    )

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(
        verbose_name='genres',
        max_length=200
    )
    slug = models.SlugField(
        max_length=100,
        unique=True,
        blank=True,
    )

    class Meta:
        verbose_name = 'жанр'
        verbose_name_plural = 'жанры'

    def __str__(self):
        return self.name


class Title(models.Model):
    name = models.CharField(
        verbose_name='title',
        max_length=200,
        null=False,
    )
    year = models.IntegerField(
        verbose_name='yaers',
        blank=True,
        null=True,
        validators=[MinValueValidator(1), MaxValueValidator(current_year())]
    )
    description = models.TextField(
        verbose_name='description'
    )
    genre = models.ManyToManyField(
        Genre,
        through='GenreTitle',
        verbose_name='genres'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        db_column='category',
        related_name='categories',
    )

    class Meta:
        verbose_name = 'произведение'
        verbose_name_plural = 'произведения'

    def __str__(self):
        return self.name


class GenreTitle(models.Model):
    genre = models.ForeignKey(
        Genre, 
        on_delete=models.CASCADE
    )
    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE
    )

    class Meta:
        db_table = 'reviews_genre_title'

    def __str__(self):
        return f'{self.genre} {self.title}'

class Review(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='reviews')
    title = models.ForeignKey(
        Title, on_delete=models.CASCADE, related_name='reviews')
    text = models.TextField()
    score = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)]
    )
    pub_date = models.DateTimeField(
        'Дата добавления', auto_now_add=True, db_index=True)

    class Meta:
        verbose_name = 'отзыв'
        verbose_name_plural = 'отзывы'


class Comment(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments')
    review = models.ForeignKey(
        Review, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    pub_date = models.DateTimeField(
        'Дата добавления', auto_now_add=True, db_index=True)

    class Meta:
        verbose_name = 'комментарий'
        verbose_name_plural = 'комментарии'
