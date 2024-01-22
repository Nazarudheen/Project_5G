from django.shortcuts import render,redirect
from BackendApp.models import CategoryDB,ProductDB
from django.utils.datastructures import MultiValueDictKeyError
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from FrontendApp.models import ContactDB
from django.contrib import messages

# Create your views here.
def Indexpage(request):
    return render(request,"index.html")
def CategoryPage(request):
    return render(request,"category.html")
def SaveCategory(request):
    if request.method=="POST":
        cn = request.POST.get('CName')
        cd = request.POST.get('CDiscription')
        img = request.FILES['CImage']
        obj = CategoryDB(Name=cn,Discription=cd,Image=img)
        obj.save()
        messages.success(request,"Category Saved Successfully...!")
        return redirect(CategoryPage)

def DisplayCategory(request):
    data = CategoryDB.objects.all()
    return render(request,"CategoryDisplay.html",{'data':data})
def EditCategory(request,cid):
    data = CategoryDB.objects.get(id=cid)
    return render(request,"CategoryEdit.html",{'data':data})
def UpdateCategory(request,cid):
    if request.method=="POST":
        cn = request.POST.get('CName')
        cd = request.POST.get('CDiscription')
        try:
            img = request.FILES['CImage']
            fs = FileSystemStorage()
            file = fs.save(img.name,img)
        except MultiValueDictKeyError:
            file = CategoryDB.objects.get(id=cid).Image
        CategoryDB.objects.filter(id=cid).update(Name=cn,Discription=cd,Image=file)
        return redirect(DisplayCategory)
def deleteCategory(request,cid):
    x = CategoryDB.objects.filter(id=cid)
    x.delete()
    messages.success(request, "Category deleted...!")
    return redirect(DisplayCategory)

def AddProduct(request):
    cat = CategoryDB.objects.all()
    return render(request,"Product.html",{'cat':cat})
def SaveProduct(request):
    if request.method=="POST":
        pc = request.POST.get('PCategory')
        pn = request.POST.get('PName')
        pp = request.POST.get('PPrice')
        pd = request.POST.get('PDiscription')
        img1 = request.FILES['PImage1']
        img2 = request.FILES['PImage2']
        img3 = request.FILES['PImage3']
        obj = ProductDB(Category=pc,Name=pn,Discription=pd,Image1=img1,Image2=img2,Image3=img3,Price=pp)
        obj.save()
        return redirect(AddProduct)
def DisplayProduct(request):
    data = ProductDB.objects.all()
    return render(request,"ProductDisplay.html",{'data':data})

def EditProduct(request,pid):
    data = ProductDB.objects.get(id=pid)
    cat = CategoryDB.objects.all()
    return render(request,"ProductEdit.html",{'data':data,'cat':cat})
def UpdateProduct(request,pid):
    if request.method=="POST":
        pc = request.POST.get('PCategory')
        pn = request.POST.get('PName')
        pp = request.POST.get('PPrice')
        pd = request.POST.get('PDiscription')
        try:
            img = request.FILES['PImage1']
            fs = FileSystemStorage()
            file1 = fs.save(img.name,img)
        except MultiValueDictKeyError:
            file1 = ProductDB.objects.get(id=pid).Image1
        try:
            img = request.FILES['PImage2']
            fs = FileSystemStorage()
            file2 = fs.save(img.name,img)
        except MultiValueDictKeyError:
            file2 = ProductDB.objects.get(id=pid).Image2
        try:
            img = request.FILES['PImage3']
            fs = FileSystemStorage()
            file3 = fs.save(img.name,img)
        except MultiValueDictKeyError:
            file3 = ProductDB.objects.get(id=pid).Image3
        ProductDB.objects.filter(id=pid).update(Category=pc,Name=pn,Discription=pd,Image1=file1,Image2=file2,Image3=file3,Price=pp)
        return redirect(DisplayProduct)
def DeleteProduct(request,pid):
    x = ProductDB.objects.filter(id=pid)
    x.delete()
    return redirect(DisplayProduct)
def LoginPage(request):
    return render(request,"AdminLogin.html")
def Admin_login(request):
    if request.method=="POST":
        un = request.POST.get('uname')
        pd = request.POST.get('passwd')

        if User.objects.filter(username__contains=un).exists():
            x = authenticate(username=un,password=pd)

            if x is not None:
                login(request,x)
                request.session['username'] = un
                request.session['password'] = pd
                messages.success(request,"Welcome")
                return redirect(Indexpage)
            else:
                messages.error(request,"Incorrect Password")
                return redirect(LoginPage)

        else:
            messages.warning(request, "Please check the username")
            return redirect(LoginPage)

def Admin_logout(request):
    del request.session['username']
    del request.session['password']
    return redirect(LoginPage)

def ContactPage(request):
    det = ContactDB.objects.all()
    return render(request,"ContactDetails.html",{'det':det})
def DeleteContact(request,ctid):
    x = ContactDB.objects.filter(id=ctid)
    x.delete()
    return redirect(ContactPage)
