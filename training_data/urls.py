from django.urls import path
from . import views

app_name = 'training_data'
urlpatterns = [
    path('user_data/', views.UserDataView.as_view(), name='user_data')
]
