from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from .models import *
import string
from .forms import *
from django.db.models import Q

# Create your views here.
def index(request):
    return render(request, 'index.html')


def signup(request):
    if (request.method == 'POST'):
        fname = request.POST.get('first_name')
        lname = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User()
        user.fName = fname

        user.lName = lname
        user.Email = email
        user.Password = password
        user.save()

        return render(request, 'index.html', context={"messages": 'Registration has been sucessful'})
    else:
        return render(request, 'userSignup.html')


def login(request):
    if (request.method == 'GET'):
        return render(request, 'Login.html')
    if (request.method == 'POST'):
        email = request.POST.get('email')
        password = request.POST.get('password')
        if (User.objects.filter(Email=email, Password=password)).exists():
            sessionvalue=User.objects.filter(Email=email, Password=password)
            for i in sessionvalue:
                request.session['userid'] = i.id
                if(request.session['userid'] ==1):
                    return render(request, 'AdminHome.html',)

            product = Spec.objects.all()
            return render(request, 'Userhome.html', context={'con': product})
        elif (Company.objects.filter(Email=email, Password=password,status="1")).exists():
            sessionvalue = Company.objects.filter(Email=email, Password=password)
            for i in sessionvalue:
                request.session['userid'] = i.id
            return render(request, 'CompanyHome.html',context={'con': request.session['userid']})
        else:
            message= "Login Failed!"
            return render(request, 'Login.html',context={'messages':message})


def CompanySignup(request):
    if (request.method == 'POST'):
        Co_name = request.POST.get('Company_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        company = Company()
        company.C_Name = Co_name

        company.Email = email
        company.Password = password
        company.status="0"
        company.save()

        return render(request, 'index.html')
    else:
        return render(request, 'CompanySignup.html')


def Addproduct(request):
    if (request.method == 'POST'):
        model = request.POST.get('model')
        network = request.POST.get('network')
        body = request.POST.get('body')
        display = request.POST.get('display')
        platform = request.POST.get('platform')
        memory = request.POST.get('memory')
        cpu = request.POST.get('cpu')
        mainCam = request.POST.get('mainCam')
        selfieCam = request.POST.get('selfieCam')
        phfeatures = request.POST.get('phfeatures')
        battery = request.POST.get('battery')
        price = request.POST.get('price')
        companyid=request.session["userid"]
        form = SpecForm(request.POST, request.FILES)

        if form.is_valid():
            # .save(commit=False)

            form.save()
        c = Spec.objects.last()
        Spec.objects.filter(id=c.id).update(model=model, network=network, body=body,
                                            display=display, platform=platform, memory=memory
                                            , cpu=cpu, mainCam=mainCam, selfieCam=selfieCam, phfeatures=phfeatures
                                            , battery=battery, price=price,companyid=companyid)

        return render(request, 'CompanyHome.html',context={'con': request.session['userid']})
    else:
        form = SpecForm()
        return render(request, 'AddProduct.html', {'form': form})


def prodectdetails(request, id):
    product = Spec.objects.filter(id=id)
    allcomments = comment.objects.filter(specid=id)
    return render(request, 'productdetails.html', context={'con': product,'allcmt':allcomments})


def compare(request, id):
    product = Spec.objects.filter(id=id)
    allproduct = Spec.objects.all()
    return render(request, 'compare.html', context={'con': allproduct, 'con2': product,})



def compareview(request,id):
    product1=Spec.objects.filter(id=id)
    id2 = request.POST.get("select")
    product2=Spec.objects.filter(id=id2)
    allproduct = Spec.objects.all()
    return render(request, 'compareview.html', context={'con': allproduct, 'con1': product1,'con2':product2})

def mycomment(request,id):
    if(request.method=='POST'):
        com=request.POST.get("comment")
        caption = request.POST.get("caption")
        if (comment.objects.filter(id=id,comments=com,caption=caption)).exists():
            return prodectdetails(request, id)

        else:
            obj=comment()
            obj.comments=com
            obj.specid=id
            obj.caption=caption
            getname=User.objects.filter(id=request.session["userid"])
            for i in getname:
                v=i.fName
            obj.username=v
            obj.save()
            return prodectdetails(request,id)
    else:
        return prodectdetails(request, id)

def logout(request):
   try:
      del request.session['username']
   except:
      pass
   return index(request)

def ALLProduct(request):
    product = Spec.objects.filter()
    allcomments = comment.objects.filter()
    return render(request, 'allproduct.html', context={'con': product})

def deleteproduct(request,id):
    Spec.objects.filter(id=id).delete()
    comment.objects.filter(id=id).delete()
    return CompanyALLProduct(request,id=request.session["userid"])

#################################..........COMPANY..........#######################################

def CompanyALLProduct(request,id):
    product = Spec.objects.filter(companyid=id)
   # allcomments = comment.objects.filter()
    return render(request, 'Companyallproduct.html', context={'con': product})

def Companyproductdetails(request, id):
    product = Spec.objects.filter(id=id)
    allcomments = comment.objects.filter(specid=id)
    return render(request, 'Companyproductdetails.html', context={'con': product, 'allcmt': allcomments})






#################################..........ADMIN..........#######################################
def AdminALLProduct(request):
    product = Spec.objects.filter()
    allcomments = comment.objects.filter()
    return render(request, 'Adminallproduct.html', context={'con': product})
def Adminproductdetails(request, id):
    product = Spec.objects.filter(id=id)
    request.session["prodectid"]=id
    allcomments = comment.objects.filter(specid=id)
    return render(request, 'Adminproductdetails.html', context={'con': product,'allcmt':allcomments})
def AdminCommentDelete(request,id):
    comment.objects.filter(id=id).delete()
    return Adminproductdetails(request,request.session["prodectid"])
def AdminALLUsers(request):
    return render(request,'AdminUsers.html')

def Adminviewallusers(request):
    from django.db.models import Q

    allusers=User.objects.filter(~Q(id=1))
    return render(request,'Adminviewallusers.html',context={'con':allusers})
def Admindeleteusers(request,id):
    User.objects.filter(id=id).delete()
    return Adminviewallusers(request)
def Adminviewallcompany(request):
    allcompany = Company.objects.all()
    return render(request,'Adminviewallcompany.html',context={'con':allcompany})

def AdminApproveCompany(request,id):
    Company.objects.filter(id=id).update(status=1)

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
def AdminRejectCompany(request,id):
    Company.objects.filter(id=id).update(status=0)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def AdminDeleteCompany(request,id):
    Company.objects.filter(id=id).delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def AdminApprovedCompanyview(request):
    allcompany = Company.objects.filter(status="1")
    return render(request, 'AdminCompanyStatusview.html', context={'con': allcompany})

def AdminRejectedCompanyview(request):
    allcompany = Company.objects.filter(status="0")
    return render(request, 'AdminCompanyStatusview.html', context={'con': allcompany})



##############################url-home#######################

def userhome(request):
    product = Spec.objects.all()
    return render(request, 'Userhome.html', context={'con': product})
def companyhome(request):

    return render(request, 'CompanyHome.html', context={'con': request.session['userid']})

def adminhome(request):
    if (request.session['userid'] == 1):
        return render(request, 'AdminHome.html', )


