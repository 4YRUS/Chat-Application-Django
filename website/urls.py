from django.urls import path
from . import views 

urlpatterns = [
    path('',views.home,name='home'),
    path('login/',views.user_login,name='login'),
    path('register/',views.user_register,name='register'),
    path('logout/',views.user_logout,name='logout'),
    path('work/<slug:slug>',views.work,name='work'),
    path('send',views.send,name='send'),
    path('work/<slug:slug>/<str:roomname>/<str:username>',views.user_work,name='user_work'),
    path('getmessages/<str:room>/',views.getmessages,name='getmessages'),
]
