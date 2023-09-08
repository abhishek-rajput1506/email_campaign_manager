from django.urls import include, path
from . import views

urlpatterns = [
     path('campaigns/', views.CampaignView().as_view(), name='campaign_list'),
]