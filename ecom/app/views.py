from django.shortcuts import render,redirect,HttpResponse
from app.models import Users,Product
from django.contrib.auth import authenticate,login,logout
from django.views import View
from . forms import CustomerRegistrationForm
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request,'home.html')

class CategoryView(View):
    def get(self,request,value):
        product=Product.objects.filter(category=value)
        title=Product.objects.filter(category=value).values('title')
        return render(request,'category.html',locals())
    
class ProductDetails(View):
    def get(self,request,pk):
        product=Product.objects.get(id=pk)

        return render(request,'productdetail.html',locals())
    
    
class CustomerRegistrationView(View):
    def get(self,request):
        form = CustomerRegistrationForm()
        return render(request,'custreg.html',locals())
    def post(self,request):
        form=CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Sign up completed!")
        else:
            messages.errors(request,"invalid Inputs!!!")
        return render(request,'custreg.html',locals())























def createuser(request):
    if request.method=="POST":
        fname=request.POST['fname']
        lname=request.POST['lname']
        e=request.POST['email']
        un=request.POST['uname']
        psw=request.POST['psw']
        Users.objects.create_user(first_name=fname,last_name=lname,email=e,username=un,password=psw,usertype="user",status=0)
        return redirect(loginpanel)
    else:
        return render(request,'register.html')
    
def loginpanel(request):
    if request.method=="POST":
        email=request.POST['uname']
        psw=request.POST['psw']
        print(email)
        user=authenticate(request,username=email,password=psw)
       
        print(user)
        if user is not None  :
            login(request,user)
            # request.session['name']=user.first_name    
            # request.session['teachid']=user.id
            # n=request.session['teachname']
            return render(request,"home.html")        
            
        else:
            
            return HttpResponse('wrong!!!')
        
    else:
        return render(request,'login.html')
    
    
    
