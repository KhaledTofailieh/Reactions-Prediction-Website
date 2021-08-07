from django.urls import path
from . import views

urlpatterns = [path('/login', views.login),
               path('/input', views.get_input_form),
               path('/reactions', views.get_reactions_prediction)]
