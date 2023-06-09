from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
# Create your views here.

def index(request):
    return render(request,"index.html",)

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        Password1 = request.POST['Password1']
        Password2 = request.POST['Password2']
        if Password1 == Password2:
            if User.objects.filter(username = username).exists():
                messages.info(request,'username already exists')
                return redirect('/register')
            elif User.objects.filter(email = email).exists():
                messages.info(request,'Email already exists')
                return redirect('/register')
            else:
                user = User.objects.create_user(username=username,email=email,password=Password1,first_name=first_name,last_name=last_name)
                user.save();
                return redirect('/login')
        
        else:
            messages.info(request,'Password doesnot matching')
            return redirect('/register')
    
    else:
        return render(request,'register.html')
    
    
   
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        Password = request.POST['Password']
        
        user = auth.authenticate(username = username,password=Password)
        print(user) 
        
        if user is not None:
            print("login")
            messages.info(request,'login sucssfully')
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'user not found')
            print("logout")
            return render(request,'login.html')

        
             
    else:
        
        return render(request,'login.html')
    
    
def logout(request):
    auth.logout(request)
    return redirect('/')
