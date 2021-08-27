from django.urls import path
from . import views

urlpatterns = [
    path('', views.start),

    path('login', views.login, name='login'),
    path('register', views.register),
    path('home', views.home),
    path('results', views.results),
    path('page_register', views.page_register),
    path('test_board', views.test_board),
    path('test_results', views.test_results),
    ]
