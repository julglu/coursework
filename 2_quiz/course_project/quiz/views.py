# Create your views here.
from django.shortcuts import render
from quiz.models import Answer, Question
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


def start(request):
    return render(request, 'index.html')


def check(request):
    question = Question.objects.get(pk=1)
    if request.method == 'POST':
        try:
            selected_answ = question.answer_set.get(pk=request.POST['answer'])
        except (KeyError, Answer.DoesNotExist):
            return render(request, 'answers.html', {'question': question})
        else:
            selected_answ.cnt += 1
            selected_answ.save()
            return render(request, 'Gist.html', {'question': question})
    else:
        return render(request, 'answers.html', {'question': question})
