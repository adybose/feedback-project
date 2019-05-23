from django.urls import path
from django.contrib import admin
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='core/home.html'), name='home'),
    path('about/', TemplateView.as_view(template_name='core/about.html'), name='about'),
    path('register/', views.RegistrationPageView.as_view(), name='register'),
    path('feedback/', views.FeedbackView.as_view(), name='feedback'),
    path('download/', TemplateView.as_view(template_name='core/about.html'), name='download'),
    # url(r'^register', views.RegistrationPageView.as_view(), name='register'),
    # url(r'^core', views.QuizView.as_view(), name='core'),
    # url(r'^result', views.result, name = 'result'),
    # url(r'^(?P<choice>[\w]+)', views.questions, name = 'questions'),
]
