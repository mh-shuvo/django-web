from django.urls import path

from . import views
urlpatterns = [
    path('home/', views.home, name='moderator_home')
]