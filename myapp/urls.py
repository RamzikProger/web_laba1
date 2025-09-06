from django.urls import path
from . import views

app_name = 'myapp'  # Добавьте эту строку

urlpatterns = [
    path('', views.index, name='index'),
]