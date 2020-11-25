from django.db import models

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    mobile = models.CharField(max_length=11, unique=True, verbose_name='手机号')
    name = models.CharField(max_length=10, verbose_name='姓名', null=True)
    avatar = models.CharField(max_length=100, verbose_name='头像', null=True)
    sex = models.CharField(max_length=50, verbose_name='性别', null=True)
    company = models.CharField(max_length=50, verbose_name='公司', null=True)
    introduce = models.CharField(max_length=50, verbose_name='信息', null=True)

    class Meta:
        db_table = 'users'
        verbose_name = '用户'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username