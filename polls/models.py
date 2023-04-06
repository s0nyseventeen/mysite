from django.db import models
from django.utils import timezone
import datetime
from django.contrib import admin


class Question(models.Model):
    print('Creating Question')
    qu_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.qu_text

    @admin.display(
        boolean=True,
        ordering='pub_date',
        description='Published recently?'
    )
    def was_published_recently(self) -> bool:
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):
    # each Choice is related to the single Question (ForeignKey)
    print('Creating Choice')
    qu = models.ForeignKey(Question, on_delete=models.CASCADE)
    ch_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.ch_text
