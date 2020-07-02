from django.shortcuts import render

from rest_framework.views import APIView
from utils.response import APIResponse

class TestAPIView(APIView):
    def get(self,request,*args,**kwargs):
        return APIResponse("行了")
