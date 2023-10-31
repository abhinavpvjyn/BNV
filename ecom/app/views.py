from django.shortcuts import render,redirect,HttpResponse
from app.models import Customer, Product
from django.contrib.auth import authenticate,login,logout
from django.views import View
from app.forms import CustomerRegistrationForm,CustomerProfileForm
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
        form = CustomerRegistrationForm(request.POST)
        return render(request,'customerregistration.html',locals())
    def post(self,request):
        form=CustomerRegistrationForm(request.POST)
        
        
        if form.is_valid():
            form.save()
            messages.success(request,"Congratulations! User Registered Successfully")
        else:
            messages.warning(request,"Invalid Input Data")
        return render(request,'customerregistration.html',locals())

class ProfileView(View):
    def get(self,request):
        form=CustomerProfileForm()
        return render(request,'profile.html',locals())
    def post(self,request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            user = request.user
            name=form.cleaned_data['name']
            locality=form.cleaned_data['locality']
            city=form.cleaned_data['city']
            mobile=form.cleaned_data['mobile']
            state=form.cleaned_data['state']
            zipcode=form.cleaned_data['zipcode']
            reg=Customer(user=user,name=name,locality=locality,mobile=mobile,city=city,state=state,zipcode=zipcode)
            reg.save()
            messages.success(request,"Address Saved successfully!")
        else:
            messages.warning(request,"Invalid input!")
        return render(request,'profile.html',locals())
    
def address(request):
    add=Customer.objects.filter(user=request.user)
    return render(request,'address.html',locals())
    






















# def createuser(request):
#     if request.method=="POST":
#         fname=request.POST['fname']
#         lname=request.POST['lname']
#         e=request.POST['email']
#         un=request.POST['uname']
#         psw=request.POST['psw']
#         Users.objects.create_user(first_name=fname,last_name=lname,email=e,username=un,password=psw,usertype="user",status=0)
#         return redirect(loginpanel)
#     else:
#         return render(request,'register.html')
    
# def loginpanel(request):
#     if request.method=="POST":
#         email=request.POST['uname']
#         psw=request.POST['psw']
#         print(email)
#         user=authenticate(request,username=email,password=psw)
       
#         print(user)
#         if user is not None  :
#             login(request,user)
#             # request.session['name']=user.first_name    
#             # request.session['teachid']=user.id
#             # n=request.session['teachname']
#             return render(request,"home.html")        
            
#         else:
            
#             return HttpResponse('wrong!!!')
        
#     else:
#         return render(request,'login.html')
    
    
    
