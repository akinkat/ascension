from django.urls import path
from . import views


app_name = 'exam'
urlpatterns = [
    path('multiple_choice_questions/<int:exam_topic>/', views.MultipleChoiceQuestionsView.as_view(), name='exam'),
]
