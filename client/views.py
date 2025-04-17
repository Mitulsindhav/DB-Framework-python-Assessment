from django.shortcuts import render,redirect
from superuser.models import client,case
from lawyer.models import instruction1,document
from .models import Review1,Document,forgotpas1
# import razorpay
from django.conf import settings
import json
# from .models import Order
from django.views.decorators.csrf import csrf_exempt
from .constants import PaymentStatus
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

def upload_document(request):
    data7 = document.objects.all()
    clientid = request.session.get('client_id')
    data5=Document.objects.filter(client_id=clientid)
    print(data5)
    if request.POST:

        title=request.POST["title"]
        upload=request.FILES["document1"]
        obj=Document(title=title,document=upload)
        obj.client_id=clientid
        obj.save()
    return render(request, 'client/document.html',{"data7":data7,"data5":data5})


# Create your views here.
# def index(request):
#     return render(request, "client/index.html")


def login(request):
    return render(request, "client/login.html")


def login2(request):
    if request.POST:
        email = request.POST['email']
        pass1 = request.POST['password']
        count = client.objects.filter(email=email, password=pass1).count()
        if count > 0:
            request.session['is_login'] = True
            request.session['client_id'] = client.objects.values('id').filter(email=email, password=pass1)[0]['id']

            return redirect('/case1')
    return render(request, "client/login.html")

def logout1(request):

        del request.session['is_login']
        return render(request, "client/login.html")


def dashboardc(request):
    return render(request, "client/dashboardc.html")


def case1(request):
    clientid = request.session.get('client_id')
    data1 = case.objects.filter(clname_id=clientid)
    return render(request, "client/case.html",{"data1":data1})




def review2(request):
    return render(request,"client/feedback.html")


def home(request):
    return render(request,"client/ind.html")


def doc1(request):
    data=Document.objects.all()
    return render(request, "client/document.html", {"data": data})

def dele(request,id):
    Document.objects.get(id=id).delete()

    return redirect('/upload_document')

def forpass(request):
    if request.POST:
        email = request.POST['email']
        count = client.objects.filter(email=email).count()
        if count > 0:
            request.session['is_login'] = True
            request.session['client_id'] = client.objects.values('id').filter(email=email)[0]['id']
            obj=forgotpas1(email=email)
            obj.save()
            return redirect('/#')

    return render(request,"client/forgotpasscl.html")