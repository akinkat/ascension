from django.shortcuts import render
from django.views import View, generic


# Create your views here.
class LearningView(generic.TemplateView):
    template_name = 'learning/learning.html'
