from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100,verbose_name='enter name of student')
    age = models.PositiveIntegerField(default=17,verbose_name='enter age of student')
    certifivate = models.FileField(upload_to='documents/',verbose_name='dowloand certificate')
    ORT_test = models.URLField(verbose_name='enter results of ORT')
    DIRECTIONS = (
        ('Backend','Backend'),
        ('Frontend','Frontend'),
        ('UI/UX','UI/UX'),
        ('not defenetetly','')
    )
    directions = models.CharField(max_length=100,choices=DIRECTIONS,default='Backend',verbose_name='choose the directions')
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}-{self.directions}'
    
    class Meta:
        verbose_name = 'student'
        verbose_name_plural = 'students'

