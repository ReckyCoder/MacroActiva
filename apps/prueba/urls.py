from django.urls import path

from . import views

app_name = 'user_app'

urlpatterns = [
    path('register/', views.UserFormView.as_view(), name='register')
]
