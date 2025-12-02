from django.db import models



bad_history = """ssentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lor"""

class AboutYou(models.Model):
    your_name = models.CharField(verbose_name="enter your name", max_length=100)
    day_birth = models.IntegerField(verbose_name="enter your day birth")
    height = models.IntegerField(verbose_name="enter your height")
    weight = models.IntegerField(verbose_name="enter your weight")
    photo = models.ImageField(
        upload_to='news/',
        verbose_name='загрузите основное фото',
        null=True,
        blank=True,          # чтобы можно было оставить пустым
    )
    regret_moment = models.TextField(
        verbose_name="enter your moment",
        max_length=500,
        default=''           # bad_history у тебя не определён, поэтому пусть будет пусто
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.your_name
    

