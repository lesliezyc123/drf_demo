from rest_framework import serializers
from rest_framework import serializers
from .models import User


# 分类序列化
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
