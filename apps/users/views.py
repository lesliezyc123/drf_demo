from django.shortcuts import render
from .models import User
from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
# Create your views here.

# 用户信息
class UserView(APIView):
    def get(self, request):
        user_id = request.user.id
        user = User.objects.get(id=user_id)
        user_serializer = UserSerializer(user)

        return Response({
            "user": user_serializer.data,
            'message':'200'
        })

    permission_classes = [IsAuthenticated]