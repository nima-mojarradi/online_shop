from django.urls import path
from .views import LoginUser,RegisterUser,UserAPIView

urlpatterns = [
    path('register/',RegisterUser.as_view(), name='register'),
    path('login/',LoginUser.as_view(),name='login'),
    path('user/',UserAPIView.as_view(),name='user')
]