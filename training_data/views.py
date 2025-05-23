from django.shortcuts import render
from django.views import View, generic


# Create your views here.
class UserDataView(generic.TemplateView):
    template_name = 'training_data/user_data.html'
    
