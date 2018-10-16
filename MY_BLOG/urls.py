from django.urls import path
from . import views

urlpatterns = [
    path('', views.signup, name='name_signup'),

    path('home/', views.welcome_home, name='welcome_home'),
    path('logout/', views.visit_again, name='visit_again')
]
