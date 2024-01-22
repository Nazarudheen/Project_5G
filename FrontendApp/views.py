from django.shortcuts import render, redirect
from BackendApp.models import CategoryDB, ProductDB
from FrontendApp.models import ContactDB, SignUpDB, CartDB
from django.contrib import messages


# Create your views here.
def Homepage(request):
    cat = CategoryDB.objects.all()
    data = CartDB.objects.filter(UserName=request.session['Name'])
    x = 0
    for i in data:
        x = x + i.Quantity
    return render(request, "Home.html", {'cat': cat,'x':x})


def All_ProductsPage(req):
    pro = ProductDB.objects.all()
    data = CartDB.objects.filter(UserName=req.session['Name'])
    x = 0
    for i in data:
        x = x + i.Quantity
    return render(req, "All_Products.html", {'pro': pro,'x':x})


def Filtered_Products(request, cat_name):
    data = ProductDB.objects.filter(Category=cat_name)
    return render(request, "FilteredProducts.html", {'data': data})


def Contact_page(request):
    return render(request, "Contact.html")


def ContactSave(request):
    if request.method == "POST":
        cn = request.POST.get('name')
        ce = request.POST.get('email')
        ca = request.POST.get('address')
        cc = request.POST.get('city')
        ct = request.POST.get('tel')
        cms = request.POST.get('msg')
        obj = ContactDB(Name=cn, Email=ce, Address=ca, City=cc, Mobile=ct, Message=cms)
        obj.save()
        messages.success(request,"Done")
        return redirect(Contact_page)


def Aboutus_page(request):
    data = CartDB.objects.filter(UserName=request.session['Name'])
    x = 0
    for i in data:
        x = x + i.Quantity
    return render(request, "AboutUs.html",{'x':x})


def ServicesPage(req):
    data = CartDB.objects.filter(UserName=req.session['Name'])
    x = 0
    for i in data:
        x = x + i.Quantity
    return render(req, "Services.html",{'x':x})


def SingleProduct_page(req, proid):
    data = ProductDB.objects.get(id=proid)
    data = CartDB.objects.filter(UserName=req.session['Name'])
    x = 0
    for i in data:
        x = x + i.Quantity
    return render(req, "SingleProduct.html", {'data': data,'x':x})


def UserSignUp_Page(req):
    return render(req, "UserSignUp.html")


def SignupPage(request):
    if request.method == "POST":
        n = request.POST.get('SName')
        e = request.POST.get('SEmail')
        p = request.POST.get('SPassword')
        i = request.FILES['SImage']
        obj = SignUpDB(Name=n, Email=e, Password=p, Image=i)
        obj.save()
        messages.success(request,"Registered")
        return redirect(UserSignUp_Page)

def LoginUser(request):
    if request.method=="POST":
        un = request.POST.get('name')
        pd = request.POST.get('password')
        if SignUpDB.objects.filter(Name=un,Password=pd).exists():
            request.session['Name']=un
            request.session['Password']=pd
            messages.success(request, "Login Successfull")
            return redirect(Homepage)
        else:
            messages.warning(request, "Username does't exist")
            return redirect(UserSignUp_Page)
    messages.error(request, "Incorrect password")
    return redirect(UserSignUp_Page)

def user_logout(request):
    del request.session['Name']
    del request.session['Password']
    messages.success(request, "Logout Successfully")
    return  redirect(UserSignUp_Page)

def SaveCart(request):
    if request.method == "POST":
        n = request.POST.get('qty')
        e = request.POST.get('uname')
        p = request.POST.get('pname')
        pr = request.POST.get('price')
        tp = request.POST.get('tprice')
        obj = CartDB( Quantity=n,UserName=e, ProName=p, Price=pr,TotalPice=tp)
        obj.save()
        messages.success(request, "Saved")
        return redirect(Homepage)

def Cart_page(request):
    data = CartDB.objects.filter(UserName=request.session['Name'])
    x = 0
    total=0
    for i in data:
        x = x+i.Quantity
        total = total+i.TotalPice
    return render(request, "Cart.html",{'data':data,'total':total,'x':x})

def deleteCartItem(req,cartid):
    x = CartDB.objects.filter(id= cartid)
    x.delete()
    return redirect(Cart_page)

def CheckoutPage(request):
    data = CartDB.objects.filter(UserName=request.session['Name'])
    x = 0
    total = 0
    for i in data:
        x = x+i.Quantity
        total = total + i.TotalPice
    return render(request,"Checkout.html",{'data':data,'total':total,'x':x})
