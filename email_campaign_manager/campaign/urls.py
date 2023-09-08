from django.urls import include, path
from . import views

urlpatterns = [
    path("", views.myView().as_view()),
]