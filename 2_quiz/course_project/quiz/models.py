from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)


class Answer(models.Model):
    question = models.ForeignKey(Question)
    answer_version = models.CharField(max_length=100)
    cnt = models.IntegerField(default=0)

    def __unicode__(self):
        return self.answer_version
