from django.shortcuts import render,HttpResponse
from rest_framework.views import APIView
# Create your views here.


from django.shortcuts import render
from .models import Campaign
from .serializers import CampaignSerializer

class Campaign(APIView):
    def get(self, request):
        campaigns = Campaign.objects.all() 
        serializer = CampaignSerializer(campaigns, many=True)
        return render(request, 'campaign_list.html', {'campaigns': serializer.data})