from django.urls import path
from . import views
from .views import *

app_name = 'user_app'

urlpatterns = [
    path('register/', views.UserFormView.as_view(), name='register'),
    path('base/', base, name='base')
]
