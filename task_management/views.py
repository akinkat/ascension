from django.shortcuts import render
from django.views import View, generic


# Create your views here.
class IndexView(generic.TemplateView):
    template_name = 'task_management/index.html'


class InterestCategoryListView(generic.TemplateView):
    template_name = 'task_management/interest_category_list.html'
