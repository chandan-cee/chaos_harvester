from django.urls import path
from . import views


urlpatterns = [
    path('', views.submit_feedback, name='submit_feedback'),
    path('all-feedback/', views.all_feedback_view, name='all_feedback'),
]