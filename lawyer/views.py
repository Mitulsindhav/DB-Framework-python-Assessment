from django.shortcuts import render,redirect
from superuser.models import client,lawyer,case
from client.models import Review1,Document
from .models import instruction1,document,forgotpas
# Create your views here.
def lawindex(request):
    lawyerid1 = request.session.get('lawyer_id')
    data=client.objects.filter(lawyername_id=lawyerid1)
    data1=data.count()
    data2=case.objects.filter(lawname_id=lawyerid1)
    data3=data2.count()

    context={
        "data": data,
        "data1": data1,
        "data2": data2,
        "data3": data3,

    }
    return render(request,"lawyer/index.html",context)


def viewcl(request):
    lawyerid = request.session.get('lawyer_id')
    data2 = client.objects.filter(lawyername_id=lawyerid)

    return render(request,"lawyer/managecl.html",{"data2":data2})


def viewcase(request):
    lawyerid = request.session.get('lawyer_id')
    data2 = case.objects.filter(lawname_id=lawyerid)


    return render(request,"lawyer/managecase.html",{"data2":data2})

def adinst(request):
    data2 = client.objects.all()
    if request.POST:
        inst1=request.POST['cltid']
        inst2=request.POST['instructions']
        obj=instruction1(inst=inst2)
        obj.client_id=inst1
        obj.save()

    return render(request,"lawyer/addinst.html",{"data2":data2})



def editinst(request,id):
    data=instruction1.objects.get(id=id)
    if request.POST:
        cl=request.POST['clientname']
        inst=request.POST['instructions']
        obj=instruction1(inst=inst,id=id)
        obj.client_id = cl
        obj.save()
        return redirect('/maninst')
    return render(request,"lawyer/edit.html",{"data":data})

def delete1(request,id):
    instruction1.objects.get(id=id).delete()
    return redirect('/maninst')

def maninst(request):
    data1=instruction1.objects.all()
    return render(request,"lawyer/manageinst.html",{"data1":data1})

def mandoc(request):
    data4=document.objects.all()
    lawyerid = request.session.get('lawyer_id')
    data5 = Document.objects.filter(client_id=lawyerid)


    return render(request,"lawyer/managedoc.html",{"data4":data4,"data5":data5})

def viewfdbc(request):
    lawyerid = request.session.get('lawyer_id')
    data11 = Review1.objects.filter(clientid_id=lawyerid)


    return render(request,"lawyer/addfeedback.html",{"data11":data11})

def login(request):
    return render(request, "lawyer/signin.html")

def login1(request):
    if request.POST:
        email=request.POST['email']
        pass1=request.POST['password']
        count=lawyer.objects.filter(email=email,password=pass1).count()
        if count>0:
            request.session['is_login']=True
            request.session['lawyer_id']=lawyer.objects.values('id').filter(email=email,password=pass1)[0]['id']
            return redirect('/lawindex')
    return render(request,"lawyer/signin.html")

def logout(request):
    del request.session['is_login']
    return render(request,"lawyer/signin.html")

def forgotpass(request):

    if request.POST:
        email=request.POST['email']
        count1 = lawyer.objects.filter(email=email).count()
        if count1>0:
            request.session['is_login']=True
            request.session['lawyer_id']=lawyer.objects.values('id').filter(email=email)[0]['id']
            obj=forgotpas(email=email)
            obj.save()
            return redirect('/#')

    return render(request,"lawyer/forgotpass.html")

def search(request):
    if request.GET:
            query=request.GET['query']

            name1=instruction1.objects.filter(client__cname=query)
    return render(request,"lawyer/search.html",{"name1":name1})

def readmore(request,id):
    data=Document.objects.get(id=id)
    return render(request,"lawyer/managedoc.html",{"data":data})
