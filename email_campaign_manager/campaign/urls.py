from django.urls import include, path
from . import views

urlpatterns = [
     path('send_campaign_messages/', views.CampaignView().as_view(), name='send_campaign'),
     path('unsubscirbe_user', views.UserView().as_view(), name='unsubscribe'),
     path('subscriber',views.UserView().as_view(), name="add_subscriber"),
]