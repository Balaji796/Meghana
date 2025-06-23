from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('view',views.view),
    path('emoji',views.emoji),
    path('home1',views.home1)
]