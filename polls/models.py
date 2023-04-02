from django.db import models
from django.utils import timezone
import datetime


class Question(models.Model):
    print('Creating Question')
    qu_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.qu_text

    def was_published_recent(self) -> bool:
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    # each Choice is related to the single Question (ForeignKey)
    print('Creating Choice')
    qu = models.ForeignKey(Question, on_delete=models.CASCADE)
    ch_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.ch_text
