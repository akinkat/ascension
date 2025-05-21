from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('task_management.urls')),
    path('learning/', include('learning.urls')),
    path('exam/', include('exam.urls')),
    path('ai_support/', include('ai_support.urls')),
    path('training_data/', include('training_data.urls')),
]
