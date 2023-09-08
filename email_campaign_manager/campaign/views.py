from django.shortcuts import render,HttpResponse
from rest_framework.views import APIView
# Create your views here.


from django.shortcuts import render
from campaign.models import Campaign,Subscriber
from .serializers import CampaignSerializer
from .controller import CampaignController

class CampaignView(APIView):
    def get(self, request):
        campaigns = Campaign.objects.all() 
        serializer = CampaignSerializer(campaigns, many=True)
        
        subscribers = Subscriber.objects.filter(active=1).values_list("email", flat=True)

        campaign_data_list = CampaignController().publish_message_to_subscribers(serializer.data, subscribers)
        
        return render(request, 'campaign_list.html', {'campaigns': campaign_data_list})