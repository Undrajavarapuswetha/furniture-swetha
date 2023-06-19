from django.shortcuts import render,redirect
from .models import Register
from admins.models import Products
from .models import Purchase
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,'index.html')

def reg(request):
    if request.method=='POST':
            cname=request.POST.get('cname')
            cemail= request.POST.get('cemail')
            paw= request.POST.get('paw')
            mno= request.POST.get('mno')
            addr= request.POST.get('addr')
            pincode = request.POST.get('pincode')
            data=Register(
                cname=cname,
                cemail=cemail,
                cpaw=paw,
                cmno=mno,
                cadd=addr,
                cpin=pincode,
            )
            data.save()
            return render(request,'index.html')
    else:
        return render(request,'Register.html')

def login(request):
    if request.method=='POST':
        try:
            email = request.POST.get('email')
            paw = request.POST.get('cpaw')
            data = Register.objects.get(cemail=email,cpaw=paw)
            request.session['userid'] = data.cemail
            print(data)
            return render(request, 'U_home.html')
        except Exception as e:
            print("Exception is:", e)
            return render(request, 'login.html')
    else:
        return render(request,'login.html')


def home(request):
    return render(request,'U_home.html')


def profile(request):
       try:
           uid=request.session['userid']
           print(uid)
           data=Register.objects.get(cemail=uid)
           return render(request,'U_profile.html',{'profile':[data]})
       except Exception as e:
           print("Exception is:",e)
           return render(request,'U_home.html')


def products(request):
    data=Products.objects.all()
    return render(request,'U_product.html',{'products': data})


def buyproduct(request,id):
    if request.method =='POST':
        uid=request.session['userid']
        cid=Register.objects.get(cemail=uid)
        product = Products.objects.get(id=id)
        data = Purchase(
            pname=product.pname,
            pcost=product.pcost,
            pcat=product.pcat,
            pquality=product.pquality,
            pdec=product.pdec,
            cid_id=cid.id,
            pid_id=id,
        )
        data.save()
        messages.success(request, 'PURCHASED SUCCESSFULLY')
        return render(request, 'U_product.html')
    else:
        messages.error(request,'NOT PURCHASE>>CHECK IT')
        return redirect('products',id=id)


def purchase(request):
    uid = request.session['userid']
    cdata = Register.objects.get(cemail=uid)
    cid = cdata.id
    data = Purchase.objects.filter(cid_id=cid)
    return render(request,'U_purchase.html',{'data': data, 'cdata': cdata})

def lastview(request):
    uid = request.session['userid']
    cdata = Register.objects.get(cemail=uid)
    cid = cdata.id
    data = Purchase.objects.filter(cid_id=cid)
    return render(request,'lastview.html',{'view':data,'cdata':cdata})

def logout(request):
    return render(request,'index.html')

def categories(request):
    return render(request,'categories.html')


def contact(request):
    return render(request,'contact.html')

def bed(request):
    return render(request,'bed.html')


def chair(request):
    return render(request,'chair.html')


def swing(request):
    return render(request,'swing.html')


def sofa(request):
    return render(request,'sofa.html')

def end(request):
    return render(request,'end.html')