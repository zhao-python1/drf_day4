from django.urls import path

from new_book import views

urlpatterns = [
    # 认证模块
    path("test/<str:id>/",views.TestAPIView.as_view()),
    path("test/", views.TestAPIView.as_view()),

    path("run/<str:id>/", views.TestPermissionAPIView.as_view()),
    path("run/", views.TestPermissionAPIView.as_view()),

    path("you/<str:id>/",views.UserLoginOrReadOnly.as_view()),
    path("you/", views.UserLoginOrReadOnly.as_view()),


    path("ren/<str:id>/",views.SenMessageAPIView.as_view()),
    path("ren/", views.SenMessageAPIView.as_view()),



]