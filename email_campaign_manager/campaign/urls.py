from django.urls import include, path
from . import views

urlpatterns = [
     path('campaigns/', views.Campaign().as_view(), name='campaign_list'),
]