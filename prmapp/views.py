from django.shortcuts import render,redirect
from .models import *
# Create your views here.
def vasthu(request):
    return render(request,"vasthuvilakku.html")
def reg(request):
    if request.method=='POST':
        username=request.POST['name']
        password=request.POST['password']
        email=request.POST['email']
        
        print("success")
        usersave=register(username=username,password=password,email=email)
        usersave.save()
        return redirect('login')

    return render(request,'reg.html')    
def login(request):
    if request.method=="POST":
        email=request.POST['email']
        password=request.POST["password"]
        logdet=register.objects.get(email=email,password=password)
        print(logdet.id)
        request.session['session1']=logdet.id
        print(request.session['session1'])
      
        return redirect("admin") 
    return render(request,'login.html')

def index(request):
    return render(request,"index.html")
def vilakku(request):
    log_det1=product.objects.filter(type='vilakku')

    return render(request,"vilakku.html",{'log':log_det1})
def para(request):
    log_det1=product.objects.filter(type='para')

    return render(request,"brass para.html",{'log':log_det1})
def house(request):
    log_det1=product.objects.filter(type='house')

    return render(request,"house.html",{'log':log_det1})
def medal(request):
    log_det1=product.objects.filter(type='medal')

    return render(request,"medal.html",{'log':log_det1})
def music(request):
    log_det1=product.objects.filter(type='music')

    return render(request,"Musical item.html",{'log':log_det1})
def photo(request):
    log_det1=product.objects.filter(type='photo')

    return render(request,"photo.html",{'log':log_det1})
def plate(request):
    log_det1=product.objects.filter(type='plate')

    return render(request,"plate.html",{'log':log_det1})
def polish(request):
    log_det1=product.objects.filter(type='polish')

    return render(request,"polish.html",{'log':log_det1})
def pooja(request):
    log_det1=product.objects.filter(type='pooja')

    return render(request,"pooja.html",{'log':log_det1})
def stand(request):
    log_det1=product.objects.filter(type='stand')

    return render(request,"stand.html",{'log':log_det1})
def temple(request):
    log_det1=product.objects.filter(type='temple')

    return render(request,"temple.html",{'log':log_det1})
def utensils(request):
    log_det1=product.objects.filter(type='utensils')

    return render(request,"utensils.html",{'log':log_det1})
def shop(request):
    log_det1=product.objects.filter(type='shop')

    return render(request,"shop.html",{'log':log_det1})


def bell(request):
    log_det1=product.objects.filter(type='bell')

    return render(request,"bell.html",{'log':log_det1})

def chain(request):
    log_det1=product.objects.filter(type='chain')

    return render(request,"chain.html",{'log':log_det1})
def gift(request):
    log_det1=product.objects.filter(type='gift')

    return render(request,"gift.html",{'log':log_det1})

def arathi(request):
    log_det1=product.objects.filter(type='arathi')

    return render(request,"arathi.html",{'log':log_det1})
def statue(request):
    log_det1=product.objects.filter(type='statue')

    return render(request,"brass statue.html",{'log':log_det1})

def admins(request):
    log_det1=product.objects.all()

    return render(request,"admin.html",{'log':log_det1})
def all(request):
    log_det1=product.objects.all()

    return render(request,"allproducts.html",{'log':log_det1})

def products(request):
    if request.method=='POST':
        name=request.POST['name']
        description=request.POST['description']
        role=request.POST['role']
        file=request.FILES['file']
        print("success")
        usersave=product(name=name,description=description,file=file,type=role)
        usersave.save()
        return admins(request)
   

    return render(request,"products.html")
def update(request,idd):
    a=product.objects.filter(id=idd)
    if request.method=='POST':
        obj=product(id=idd)
        obj.name=request.POST["name"]
        obj.description=request.POST["description"]
        obj.file=request.FILES['file']
        obj.role=request.POST['role']
        obj.save()
        return admins(request) 
    return render(request,"update.html",{'ob':a})
def delete(request,idd):
    obj=product.objects.filter(id=idd).delete()
    return admins(request)

