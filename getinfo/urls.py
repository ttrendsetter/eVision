from django.urls import path
from . import views

urlpatterns = [
    path('meta/', views.main_data_view, name='meta')
]
