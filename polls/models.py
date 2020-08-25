import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

class Question(models.Model):
    question_text = models.CharField('Question', max_length=200)
    def __str__(self):
        return self.question_text
    pub_date = models.DateTimeField('Date de publication')
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Publié récemment?'

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField('Choix', max_length=200)
    def __str__(self):
        return self.choice_text
    votes = models.IntegerField(default=0)
    