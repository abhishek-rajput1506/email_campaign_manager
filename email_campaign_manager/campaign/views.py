from django.shortcuts import render,HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.


from django.shortcuts import render
from campaign.models import Campaign,Subscriber
from .serializers import CampaignSerializer
from .controller import CampaignController, SubscriberController

class CampaignView(APIView):
    def get(self, request):
        campaigns = Campaign.objects.all() 
        serializer = CampaignSerializer(campaigns, many=True)
        
        subscribers = Subscriber.objects.filter(active=1).values_list("email", flat=True)

        campaign_data_list = CampaignController().publish_message_to_subscribers(serializer.data, subscribers)
        
        return render(request, 'campaign_list.html', {'campaigns': campaign_data_list})
    
class USerView(APIView):
    def put(self, request):
        email = request.data.get('email')

        if not email:
            responsse = {
                "status": "Failure",
                "message": "Please provide a email"
            }
            return Response({}, status=status.HTTP_400_BAD_REQUEST)
        
        response = SubscriberController().unsubscribe_user(email)

        return Response(response, status=status.HTTP_200_OK)