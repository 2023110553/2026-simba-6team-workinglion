from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('onboarding/', views.onboarding, name='onboarding'),
    path('signup_login/', views.signup_login, name='signup_login'),
]