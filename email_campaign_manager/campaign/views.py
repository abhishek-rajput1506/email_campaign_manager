from django.shortcuts import render,HttpResponse
from rest_framework.views import APIView
# Create your views here.


class myView(APIView):
    def get(self, request):
        return HttpResponse("Setup")