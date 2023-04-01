from django.db import models


class Question(models.Model):
    print('Creating Question')
    print(f'{dir()=}')
    qu_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    # each Choice is related to the single Question (ForeignKey)
    print('Creating Choice')
    print(f'{dir()=}')
    qu = models.ForeignKey(Question, on_delete=models.CASCADE)
    ch_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
