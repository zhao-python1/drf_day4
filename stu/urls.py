from django.urls import path

from stu import views

urlpatterns = [

    path("test/<str:id>/",views.TestAPIView.as_view()),
    path("test/", views.TestAPIView.as_view()),

]