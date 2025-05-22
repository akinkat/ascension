from django.shortcuts import render
from django.views import View, generic


# Create your views here.
class MultipleChoiceQuestionsView(generic.TemplateView):
    template_name = 'exam/exam.html'
