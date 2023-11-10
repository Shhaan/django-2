from django.shortcuts import render,redirect
from  django.contrib import messages,auth
from django.contrib.auth.models import User
from django.db.models import Q,Avg,Count       #used to find queris in django
from pprint import pprint
# Create your views here.
def myadminlogin(request):
    if request.user.is_authenticated and request.user.is_superuser:
           return redirect('myadmin')
    if request.method == 'POST':
        password = request.POST['password']
        username = request.POST['username']
        user = User.objects.filter(username=username)
        if not user.exists():
            messages.info(request,'Account not found')
            return redirect('myadminlogin')
        
            
        user = auth.authenticate(username=username,password=password)
        if user is not None and user.is_superuser:
            auth.login(request,user)
            return redirect('myadmin')
        else:
            if  user is None:
                messages.info(request,'Invalid password')
                
            else:
                messages.info(request,'not a superuser')
        return redirect('myadminlogin')        
    return render(request,'adminlogin.html')    
     
def myadmin(request):
    if not request.user    or request.user.is_superuser==False: 
        return redirect('myadminlogin')  
    
    return render(request,'myadmin.html')    
def user(request):
    if not request.user    or request.user.is_superuser==False: 
        return redirect('myadminlogin')  
    user = User.objects.all() 
    if request.method == 'POST':
        username = request.POST['username']
    
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        id = request.POST['id']
        is_staff = 'is_staff' in request.POST
        is_superuser = 'is_superuser' in request.POST
        e_user = User.objects.filter(id=id)
        exist_email = User.objects.filter(email=email).first()
        exist_username = User.objects.filter(username=username).first()
        if exist_username:
            if username != e_user[0].username and username != 'default_username':
                messages.info(request, 'Username already exists in the database.')
                return redirect('myuser')
        if exist_email:
            if email != e_user[0].email and email != 'default_email':
                messages.info(request, 'Email already exists in the database.')
                return redirect('myuser')
        if username != e_user[0].username and username != 'default_username':
            e_user.update(username=username)
        if email != e_user[0].email and email != 'default_email':
            e_user.update(email=email)   
        e_user.update(last_name=last_name, first_name=first_name, is_staff=is_staff, is_superuser=is_superuser)
    return render(request,'user.html',{'a_user':user})     
def deleteuser(request):
    if request.method == 'POST':
        d_id = request.POST['d_id']
        User.objects.filter(id=d_id).delete()
        return redirect('myuser')

def adminlogout(request):
    auth.logout(request)
    return redirect('myadminlogin')
def adduser(request):
    if request.method == 'POST':
        firstname =request.POST['firstname']
        last_name =request.POST['last_name']
        username =request.POST['username']
        email =request.POST['email']
        password1 =request.POST['password1']
        password2 =request.POST['password2']
        if password1 ==password2:
            if  User.objects.filter(username=username).exists() :
                messages.info(request,'username taken')
                return redirect('adduser')
            elif not username:
                messages.info(request,'Username must be entered')
                return redirect('adduser')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Try a different email')
                return redirect('adduser')
            elif not firstname:
                messages.info(request,'First name must be entered')
                return redirect('adduser')
            
            elif not password1:
                messages.info(request,'Password must be entered')
                return redirect('adduser')
            
            else:
                user = User.objects.create_user(first_name=firstname,last_name=last_name,password=password1,email=email,username=username)
                user.save()
                messages.info(request,'user added')
                return redirect('adduser')
        else:
            messages.info(request,'Both password must same')    
            return redirect('adduser')
    return render(request,'adduser.html')
def mysearch(request):
    searched = None
    if request.method =='POST':
        search = request.POST['search']
        if not search :
            return redirect('myuser')
        else:
            searched = User.objects.filter(username=search)
    return render(request,'user.html',{'searched':searched})  
