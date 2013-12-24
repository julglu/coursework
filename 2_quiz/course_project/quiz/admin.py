from django.contrib import admin
from quiz.models import *
from django.contrib.contenttypes import generic


class QuestionsAdmin(admin.ModelAdmin):
    list_display = ['question_text']


class AnswersAdmin(admin.ModelAdmin):
    list_display = ['question', 'answer_version', 'cnt']


admin.site.register(Question, QuestionsAdmin)
admin.site.register(Answer, AnswersAdmin)
