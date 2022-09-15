from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Rooms,Message
from django.http import HttpResponse,JsonResponse
from django.contrib import auth
from django.contrib.auth.models import User
# Create your views here.

@login_required(login_url='login')
def homepage(request):
    room = Rooms.objects.all()
    return render(request,"chat.html",
                  {"room":room}
)
 



def room(request,room,name):
    room_ = Rooms.objects.filter(id=room)
    room_id = Rooms.objects.get(id=room)
    message = Message.objects.filter(room=room_id)
    
    
    return render(request,'room.html',{'room':room_,'message':message,'room_':room,'name':name})

  
  
  
  
def send(request): 
    
    message = request.POST.get('text')
    room = request.POST.get('room') 
    get_room = Rooms.objects.get(id=int(room))
    get_user = auth.get_user(request)
    new_message = Message.objects.create(text=message,user=get_user,room=get_room)
    new_message.save()
    print(message)
    print(get_room)
    print(get_user)
    return HttpResponse('message send successfully')
  
  
  
  
  
  
def getMessages(request,room):
    room = Rooms.objects.get(id=room)
    text = Message.objects.filter(room=room)
    allMessages = []
    for item in text:
        data = {
            'picture':item.user.profile.pic.url,
            'text':item.text,
            'time':item.time
            }
        allMessages.append(data)
        
    
    return JsonResponse({"messages":allMessages})
      
  
  
  
  
  
