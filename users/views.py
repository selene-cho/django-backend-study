from django.shortcuts import render
from rest_framework.views import APIView
from .models import User
from .serializers import UserSerializer
from rest_framework.response import Response
# Create your views here.


# Attendance(출결관리)
# - User
# - Class
# - 날짜 (date)
# - 출결여부 (is_attendance)

class Users(APIView):
    def get(self, request):
        users = User.objects.all() # object
        serializer = UserSerializer(users, many=True) # json
        
        return Response(serializer.data)