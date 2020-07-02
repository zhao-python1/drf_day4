# 认证模块
from rest_framework.authentication import BaseAuthentication

from rest_framework import exceptions
from new_book.models import User


#认自定义方法类认证模块的
class MyAuth(BaseAuthentication):

   #重写authentication
   def authenticate(self, request):
       # 获取认证信息
       auth = request.META.get('HTTP_AUTHORIZATION', None)
       print(auth)
       if auth is None:
           # 代表游客
           return None

       #设置认证新消息的规则  “auth 认证信息”
       auth_list = auth.split()
       #JI检验是否合法，是不是两段式 第一个不是auth报错
       if not (len(auth_list) == 2 and auth_list[0].lower()=="auth"):
           raise exceptions.AuthenticationFailed("认证信息有误，认真失败")

       #如果成功则解析出用户 规定认证信息必须为abc.admin.123
       if auth_list[1] != "abc.marry.123":
           raise exceptions.AuthenticationFailed("用户信息校验失败")

       #最后检验数据库是否存在此用户
       user = User.objects.filter(username="zhao").first()
       if not user:
           raise exceptions.AuthenticationFailed("用户信息不存在")
       return (user,None)






