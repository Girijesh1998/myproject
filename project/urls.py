from django.urls import path
from . import views
urlpatterns = [
    path('project/', views.project, name='project'),
    path('project1/', views.project1, name='project1'),
]
