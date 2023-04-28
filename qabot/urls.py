from django.urls import path
from . import views

urlpatterns = [
    path('qabot/', views.qabot, name='qabot'),
]
