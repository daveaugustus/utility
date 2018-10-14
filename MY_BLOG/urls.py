from django.urls import path
from . import views

urlpatterns = [
    path('', views.signup, name='name_signup'),
    path('', views.index, name = 'name_index'),
]
