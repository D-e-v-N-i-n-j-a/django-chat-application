from. import views
from django.urls import path

urlpatterns = [
    path('',views.homepage,name="chat"),
    path('room/<str:room>/<str:name>/',views.room,name="room"),
    path('getMessages/<str:room>/',views.getMessages,name="getMessages"),
    path('send',views.send,name="send"),
]



