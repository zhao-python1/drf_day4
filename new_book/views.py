from django.contrib.auth.models import Group, Permission
from django.shortcuts import render
from rest_framework.request import Request
from rest_framework.throttling import UserRateThrottle
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework import settings
from rest_framework.authentication import BasicAuthentication

from new_book.models import User
from new_book.authentications import MyAuth
from new_book.permissions import Mypermissions
from new_book.throttle import SendMessageRate
from utils.response import APIResponse



class TestAPIView(APIView):
    authentication_classes =[MyAuth]
    def get(self,request,*args,**kwargs):


        # #查用户
        user = User.objects.first()
        # #根据用户查角色
        # print(user.groups.first())

        # #根据用户获取用户对应的权限
        # print(user.user_permissions.first())
        #
        # #获取角色
        # group = Group.objects.first()
        # print(group)
        # #通过角色获取对应的权限
        # print(group.permissions.first().name)
        # #根据角色获取对应的用户
        # print(group.user_set.first().username)

        # #获取权限
        # permission = Permission.objects.filter(pk=9).first()
        # print(permission.name)
        # #根据权限获取用户
        # print(permission.user_set.first().username)
        # #根据权限获取角色
        # per = Permission.objects.filter(pk=5).first()
        # print(permission.group_set.first.name)

        return APIResponse("行了")


class TestPermissionAPIView(APIView):
    "认证后才能访问"
    authentication_classes = [MyAuth]
    permission_classes = [IsAuthenticated]

    def get(self,request,*args,**kwargs):
        return APIResponse('登录访问成功')


class UserLoginOrReadOnly(APIView):
    '''登录科协，游客只读'''
    throttle_classes = [UserRateThrottle]

    def get(self,request,*args,**kwargs):
        return APIResponse("该操作访问成功")
    def post(self,request,*args,**kwargs):
        return APIResponse("写操作")



class SenMessageAPIView(APIView):
    throttle_classes = [SendMessageRate]

    def get(self,request,*args,**kwargs):
        return APIResponse("读操作成功，但是不能写")
    def post(self,request,*args,**kwargs):
        return APIResponse("写操作")