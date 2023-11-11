from django.shortcuts import render,redirect
from .models import game,feeds
from  django.contrib import messages,auth
from django.contrib.auth.models import User
# Create your views here.
def home(request):
    obj = game.objects.all()
    return render(request,'home.html',{'obj':obj})
def snake(request):
    if request.user.is_authenticated == False:
        return redirect('login')
    else:
      return render(request,'snake.html')
    
def flappy(request):
    if request.user.is_authenticated == False:
        return redirect('login')
    else:
        
      return render(request,'flappy.html')
def feedback(request):
    if request.user.is_authenticated == False:
        return redirect('login')
    else:
        if request.method == 'POST':   
            feed = request.POST['feed'] 
            frange = request.POST['nonein']     
            if feed.strip():
                obj = feeds(feedback=feed,ratings = frange)
                obj.save()
            else:
                messages.info(request,'Enter something in feedback')
            return redirect('feedback')    
        
    return render(request,'feedback.html')
def about(request):
    return render(request,'about.html')

def login(request):
    if request.user.is_authenticated:
           return redirect('home')  
    if request.method == 'POST':
        password = request.POST['password']
        username = request.POST['username']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.info(request,'Enter a valid user')
            redirect('login')
         
    else:
        return render(request,'login.html')    
    return render(request,'login.html')
def register(request):
    if request.method == 'POST':
        first_name =request.POST['first_name']
        last_name =request.POST['last_name']
        username =request.POST['username']
        email =request.POST['email']
        password1 =request.POST['password1']
        password2 =request.POST['password2']
        if password1 ==password2:
            if  User.objects.filter(username=username).exists() :
                messages.info(request,'username taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Try a different email')
                return redirect('register')
            elif not first_name:
                messages.info(request,'First name must be entered')
            elif not password1:
                messages.info(request,'Password must be entered')
            
            else:
                user = User.objects.create_user(first_name=first_name,last_name=last_name,password=password1,email=email,username=username)
                user.save()
                if user is not None:
                    auth.login(request, user)
                    return redirect('home')
        else:
            messages.info(request,'Both password must same')    
            return redirect('register')
        
    return render(request,'register.html')
def logout(request):
    auth.logout(request)
    return redirect('login')