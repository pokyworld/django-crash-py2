# -*- coding: utf-8 -*-
# from __future__ import unicode_literals
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
from .models import Question, Choice

# Get Questions and display then
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'title': 'Poll Questions', 'latest_question_list': latest_question_list }
    return render(request, 'polls/index.html', context)

# Show specific question and choices
def details(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
        context = { 'title': 'Choose your favorite', 'question': question }
    except Question.DoesNotExistList:
        raise Http404("Question does not exists")

    return render(request, 'polls/detail.html', context)

# Get question and display results

def results(request, question_id):
    # return HttpResponse("Results")

    try:
        question = get_object_or_404(Question, pk=question_id)
        context = { 'title': 'Results so far...', 'question': question }
    except Question.DoesNotExistList:
        raise Http404("Question does not exists")

    return render(request, 'polls/results.html', context)


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

