from django.shortcuts import render
from django.http import JsonResponse
from .models import User
from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
import re
# Create your views here.

# User用户信息
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


# 注册用户
class newUserView(APIView):
    def post(self, request):

        surname = request.data.get("surname")
        personal = request.data.get("personal")
        name = str(surname) + str(personal)
        sex = request.data.get("sex")
        username = request.data.get("username")
        email = request.data.get("email")
        password = request.data.get("password")

        if not all([username, password, email, sex, surname, personal]):
            return JsonResponse({'status': False, 'msg': '数据填写不完整'})

        if not re.match('^[a-zA-Z0-9_-]{5,20}$', username):
            return JsonResponse({'status': False, 'msg': '用户名为5-20个字符'})

        if User.objects.filter(username=username).count() > 0:
            return JsonResponse({'status': False, 'msg': '用户名已经存在'})

        if User.objects.filter(email=email).count() > 0:
            return JsonResponse({'status': False, 'msg': '邮箱已经存在'})

        if not re.match('^[0-9A-Za-z]{6,20}$', password):
            return JsonResponse({'status': False, 'msg': '密码为6-20个字符'})

        User.objects.create_user(username=username, email=email, password=password,name=name,sex=sex)

        return Response({'status': True, 'msg': '新增成功'})


# 登录
class signUserView(APIView):
    def post(self, request):
        name_eamil = request.data.get("username")
        password = request.data.get("password")

        if User.objects.filter(Q(username=name_eamil) | Q(email=name_eamil)).count() == 0:
            return JsonResponse({'status': False, 'msg': '用户名或者账号不存在'})

        user_get = User.objects.get(Q(username=name_eamil) | Q(email=name_eamil))

        user = authenticate(request, username=user_get.username,password=password)
        if  user == None:
            return JsonResponse({'status': False, 'msg': '密码不正确'})

        data = {
            'username': user.username,
            'password': password
        }
        return Response({'status': True, 'msg': '登录成功',"data":data})
