from django.shortcuts import render
from.models import Products
from user.models import Purchase
from user.models import Register


from PIL import Image
from django.core.files import File



# Create your views here.
def alogin(request):
    if request.method=='POST':
        try:
            email=request.POST.get('email')
            paw=request.POST.get('paw')
            if email=='admin@gmail.com' and paw=='admin':
                return render(request, 'a_home.html')
            else:
                return render(request, 'a_home.html')
        except Exception as e:
            print('Exception is:",e')
            return render(request,'a_home.html')
    else:
        return render(request,'a_login.html')

def ahome(request):
    return render(request, 'a_home.html')



def addproduct(request):
        if request.method == 'POST':
            try:
                pname = request.POST.get('pname')
                pcat = request.POST.get('pcat')
                pcost = request.POST.get('pcost')
                pquality = request.POST.get('pquality')
                pdec = request.POST.get('pdec')
                pimage=request.FILES['pimage']
                print(pimage)
                data = Products(
                    pname=pname,
                    pcat=pcat,
                    pcost=pcost,
                    pquality=pquality,
                    pdec=pdec,
                    pimage=pimage
                )
                data.save()
                return render(request, 'a_viewproduct.html')
            except Exception as e:
                print("Exception is:", e)
                return render(request, 'a_home.html')
        else:
            return render(request, 'a_addproduct.html')




def viewproduct(request):
    data=Products.objects.all()
    print(data)
    return render(request,'a_viewproduct.html',{'data':data})




def profile1(request):
    try:
        data = Products.objects.all()
        return render(request, 'a_viewproduct.html', {'profile4': [data]})
    except Exception as err:
        print("EXCEPTION IS:", err)
        return render(request, 'a_addproduct.html')


def alogout(request):
    return render(request, 'index.html')


def alastview(request):
    uid = request.session['userid']
    cdata = Register.objects.all()
    cid = cdata
    data = Purchase.objects.all()
    return render(request, 'a_lastview.html',{'view': data, 'cdata': cdata})
def HOME(request):
    return render(request,'HOME.html')