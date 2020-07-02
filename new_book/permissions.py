#权限模块
from rest_framework.permissions import BasePermission

from new_book.models import User


#自定义地方法类的权限，模块的

class Mypermissions(BasePermission):
    '''

    有权限返回ture
    无趣权限放回false
    登录能写，游客能读
    '''

    def has_permission(self,request,view):
        #若果只读的话 全都能访问
        if request.method in ("GET",'HEAD','OPTIONS'):
            return True
        username = request.data.get("username")
        #如果是写的操作，就要判断用户是否登陆了

        user = User.objects.filter(username=username).first()
        print(user)
        if user:
            return True
        return False