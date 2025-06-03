from django.urls import path

from . import views


app_name = 'task_management'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('interest_category_list/', views.InterestCategoryListView.as_view(), name='interest_category_list'),
]
