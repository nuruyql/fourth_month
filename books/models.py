from django.db import models
from django.core.validators import (
    MinValueValidator,
    MaxValueValidator,
    MinLengthValidator,
)


bad_history = """ssentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lor"""


class AboutYou(models.Model):
    author = models.CharField(verbose_name="enter author this book", max_length=100, default='unknown')
    day_made = models.IntegerField(verbose_name="when was created this book", default=2000)
    pages = models.IntegerField(verbose_name="enter how many pages", default=200)
    jenre = models.TextField(verbose_name="enter jenre", default='romcom')
    photo = models.ImageField(
        upload_to='news/',
        verbose_name='загрузите основное фото',
        null=True,
        blank=True,
    )
    discription = models.TextField(
        verbose_name="enter your moment",
        max_length=500,
        default='',
        blank=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author

    class Meta:
        verbose_name = 'book'
        verbose_name_plural = 'books ab'


class Reviews(models.Model):
    choose = models.ForeignKey(
        AboutYou,
        on_delete=models.CASCADE,
        related_name='review',
        verbose_name='book',
    )

    # значение в db 1–5 , отображаемое сердечки
    MARKS = (
        (1, "♥️"),
        (2, "♥️♥️"),
        (3, "♥️♥️♥️"),
        (4, "♥️♥️♥️♥️"),
        (5, "♥️♥️♥️♥️♥️"),
    )

    marks = models.IntegerField(
        verbose_name="choose marks",
        choices=MARKS,
        default=4,
        validators=[
            MinValueValidator(1, message="Ставьте оценку только от 1 до 5"),
            MaxValueValidator(5, message="Ставьте оценку только от 1 до 5"),
        ],
    )

    text = models.TextField(
        verbose_name='enter review',
        validators=[
            MinLengthValidator(200, message="Минимум 200 символов!")
        ],
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.choose} — {self.marks}'
