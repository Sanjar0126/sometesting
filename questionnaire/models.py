from django.db import models
from django.utils import timezone


# Create your models here.
class Test(models.Model):
    created_at = models.DateTimeField(default=timezone.now)
    title = models.CharField(max_length=200)
    owner = models.ForeignKey('auth.User', related_name='tests', on_delete=models.CASCADE)
    solved = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ['created_at']


class Question(models.Model):
    test = models.ForeignKey('Test', related_name='questions', on_delete=models.CASCADE)
    question_text = models.TextField()
    point = models.IntegerField(default=1)

    def __str__(self) -> str:
        return self.question_text


class Answer(models.Model):
    question = models.ForeignKey('Question', related_name='answers', on_delete=models.CASCADE)
    answer = models.CharField(max_length=255)
    is_true = models.BooleanField(default=False)

    def __str__(self):
        return self.answer
