from django.shortcuts import render, redirect
from .models import category, lawyer, case, client,court,User
from lawyer.models import instruction1,forgotpas
from client.models import Review1,forgotpas1
# from myapp.models import contactEnquiry
from django.contrib import messages
import random   
# import requests


# Create your views here.
def home(request):

    data4 = lawyer.objects.all()
    data5 = data4.count()
    data = client.objects.all()
    data1 = data.count()
    data2 = case.objects.all()
    data3 = data2.count()
    lawyer_gender_male = lawyer.objects.filter(gender='Male').count()
    lawyer_gender_female = lawyer.objects.filter(gender='Female').count()
    client_gender_male=client.objects.filter(gender='Male').count()
    client_gender_female =client.objects.filter(gender='Female').count()
    print(client_gender_female)
    context={
        "data": data,
        "data1": data1,
        "data2": data2,
        "data3": data3,
        "data4": data4,
        "data5": data5,
        "client_gender_male":client_gender_male,
        "client_gender_female":client_gender_female,
        "lawyer_gender_male":lawyer_gender_male,
        "lawyer_gender_female":lawyer_gender_female

    }

    return render(request, "admin/dashboard.html",context)


def user(request):
    condata=contactEnquiry.objects.all
    return render(request, "admin/user.html",{"condata":condata})


def category1(request):
    if request.POST:
        cattname = request.POST['catname']
        catdisc = request.POST['catdis']
        obj1 = category(catname=cattname, catdisc=catdisc)
        obj1.save()
        return redirect('/#')
    return render(request, "admin/category.html")





def edit4(request, id):
    data4 = category.objects.get(id=id)
    if request.POST:
        cattname = request.POST['catename']
        catdsc = request.POST['Disc']
        obj10 = category(catname=cattname, catdisc=catdsc, id=id)
        obj10.save()
        return redirect('/mancategory')
    return render(request, "admin/update4.html", {"data4": data4})


def delete4(request, id):
    category.objects.get(id=id).delete()
    return redirect('/mancategory')


def feedback(request):
    data1 = Review1.objects.all()
    return render(request, "admin/feedback.html", {"data1": data1})


def lawyer1(request):
    data = category.objects.all()
    if request.POST:
        lawname = request.POST['lawyer']
        cat = request.POST['catlaw']
        pdetail1 = request.POST['detail1']
        experience = request.POST['experiance']
        location = request.POST['location']
        email1 = request.POST['email']
        passw = request.POST['password']
        ph = request.POST['phone']
        gender=request.POST['gender']
        obj2 = lawyer(lname=lawname, category=cat, pdetail=pdetail1, experience=experience, location=location,
                      email=email1, password=passw, phone=ph,gender=gender)
        obj2.save()
        messages.success(request,"lawyer added successfully")



    return render(request, "admin/lawyer.html", {"data": data})





def edit1(request, id):
    data3 = lawyer.objects.get(id=id)
    data=category.objects.all()
    if request.POST:
        lawname = request.POST['lawyer']
        cat = request.POST['catname']
        detail = request.POST['detail1']
        experience = request.POST['experiance']
        location = request.POST['location']
        email1 = request.POST['email']
        password = request.POST['password']
        ph = request.POST['phone']
        gender = request.POST['gender']
        objl = lawyer(lname=lawname, category=cat, pdetail=detail, experience=experience, location=location,
                      email=email1, password=password, phone=ph,gender=gender, id=id)
        objl.save()
        return redirect('/manlaw')
    return render(request, "admin/update.html", {"data3": data3,"data":data})


def delete1(request, id):
    lawyer.objects.get(id=id).delete()
    return redirect('/manlaw')


def case1(request):
    data = lawyer.objects.all()
    data2 = client.objects.all()
    data3 = category.objects.all()
    data4 = court.objects.all
    if request.POST:
        casename1 = request.POST['casename2']
        casedt = request.POST['cdate']
        catname = request.POST['catname']
        cltname = request.POST['cltname']
        lawname = request.POST['lawname1']
        cou1 = request.POST['court']
        obj3 = case(casename=casename1, casedate=casedt)
        obj3.catgname_id = catname
        obj3.clname_id = cltname
        obj3.lawname_id  = lawname
        obj3.court2_id =cou1


        obj3.save()
        return redirect('/#')

    return render(request, "admin/case.html", {'data': data, "data2": data2, "data3": data3,"data4":data4})





def edit3(request, id):
    data = case.objects.get(id=id)
    data2=client.objects.all
    datac=lawyer.objects.all
    data3=category.objects.all

    if request.POST:
        casename1 = request.POST['casename2']
        casedt = request.POST['cdate']
        catname = request.POST['catname']
        cltname = request.POST['cltname']
        lawname = request.POST['lawname1']
        cou1 = request.POST['court']
        obj3 = case(casename=casename1, casedate=casedt, id=id)
        obj3.catgname_id = catname
        obj3.clname_id = cltname
        obj3.lawname_id = lawname
        obj3.court2_id =cou1
        obj3.save()
        return redirect('/mancase')
    return render(request, "admin/update3.html", {"data": data,"data2":data2,"datac":datac,"data3":data3})


def delete3(request, id):
    case.objects.get(id=id).delete()
    return redirect('/mancase')

    return render(request, "admin/update3.html")


def client1(request):
    data = lawyer.objects.all()
    data1=court.objects.all()
    if request.POST:
        cl1 = request.POST['cll1']
        email = request.POST['email1']
        password1 = request.POST['password']
        phone = request.POST['phone']
        dob = request.POST['dob']
        address = request.POST['address']
        city = request.POST['city']
        state = request.POST['state']
        postcode = request.POST['postcode']
        gender = request.POST['gender']
        lid = request.POST['lawyer']
        cou2=request.POST['court']


        obj4 = client(cname=cl1, email=email, password=password1, phone=phone, dob=dob, add=address, city=city,
                      state=state,
                      gender=gender, postalcode=postcode)
        obj4.lawyername_id = lid
        obj4.court1_id=cou2
        obj4.save()
        return redirect('/#')
    return render(request, "admin/client.html", {'data': data,"data1":data1})




def edit2(request, id):
    data6 = client.objects.get(id=id)
    datal=lawyer.objects.all()

    if request.POST:
        cl2 = request.POST['cltname2']
        email = request.POST['email1']
        password2 = request.POST['clpassword']
        phone = request.POST['phone']
        dob = request.POST['dob']
        address = request.POST['address']
        city = request.POST['city']
        state = request.POST['state']
        postcode = request.POST['postcode']
        Gender = request.POST['gender']
        cou1=request.POST['court']
        lname2 = request.POST['lawyer']
        obje = client(cname=cl2, email=email, password=password2, phone=phone, dob=dob, add=address, city=city,
                      state=state,
                      gender=Gender, postalcode=postcode, id=id)
        obje.lawyername_id = lname2
        obje.court1_id=cou1
        obje.save()
        return redirect('/manclient')
    return render(request, "admin/update2.html", {"data6": data6,"datal":datal})


def delete2(request, id):
    client.objects.get(id=id).delete()
    return redirect('/manclient')


def manlaw(request):
    data3 = lawyer.objects.all
    return render(request, "admin/manlaw.html", {"data3": data3})

def forgotlawyer(request):
    data3=forgotpas.objects.all()
    return render(request,"admin/forgotlawyer.html",{"data3":data3})

def forgotclient(request):
    data4=forgotpas1.objects.all()
    return render(request,"admin/forgotcl.html",{"data4":data4})


def manappointment(request):
    return render(request, "admin/manappointment.html")


def mancase(request):
    data4 = case.objects.all
    return render(request, "admin/mancase.html", {"data4": data4})


def mancategory(request):
    data2 = category.objects.all
    return render(request, "admin/mancategory.html", {"data2": data2})


def manclient(request):
    data5 = client.objects.all
    return render(request, "admin/manclient.html", {"data5": data5})


def maninstruction(request):
    data = instruction1.objects.all()
    return render(request, "admin/maninstruction.html", {"data": data})


def manpayment(request):
    data=Order.objects.all()
    return render(request, "admin/manpayment.html",{"data":data})





def search1(request):
    if request.GET:
        quer = request.GET["query1"]
        name11 = lawyer.objects.filter(lname=quer)
    return render(request, "admin/lawsearch.html", {"name11": name11})


def search2(request):
    if request.GET:
        que1 = request.GET["clsearch"]
        name1 = client.objects.filter(cname=que1)
    return render(request, "admin/cltsearch.html", {"name1": name1})


def search3(request):
    if request.GET:
        que2 = request.GET["casearch"]
        name2 = case.objects.filter(casename=que2)
    return render(request, "admin/caseserch.html", {"name2": name2})


def search4(request):
    if request.GET:
        que3 = request.GET["catsearch"]
        name3 = category.objects.filter(catname=que3)
    return render(request, "admin/catsearch.html", {"name3": name3})


def notification(request):
    return render(request,"admin/user.html")

def court1(request):
    if request.POST:
        cou=request.POST['courtname1']
        obj=court(courtname=cou)
        obj.save()
    return render(request, "admin/court.html")


def register(request):
     if request.method=="POST":
        try:
            User.objects.get(email=request.POST['email'])
            msg='Email Alrady Registrade'
            return render(request,'admin/register.html',{'msg':msg})
        except:
            if request.POST['password']==request.POST['cpassword']:
        
                User.objects.create(
                    fname=request.POST['fname'],
                    lname=request.POST['lname'],
                    email=request.POST['email'],
                    mobile=request.POST['mobile'],
                    address=request.POST['address'],
                    password=request.POST['password'],
                   profile_picture=request.FILES['profile_picture'],
                    
                    
                )
                msg="User Sign Up Successfully"
                return render(request,'admin/register.html',{'msg':msg})
            else:   
                msg="password & confirm password Does not match."
                return render(request,'admin/register.html',{'msg':msg})
     else:  
        return render(request,'admin/register.html')
def login(request):
    if request.method=="POST":
        try:
            user=User.objects.get(email=request.POST['email'])
            if user.password==request.POST['password']:
                request.session['fname']=user.fname+" "+user.lname
                request.session['email']=user.email
                request.session['profile_picture']=user.profile_picture.url
                return render(request,'admin/Dashbord.html')
            else:
                msg="Incorrect Password"
                return render(request,'admin/login.html',{'msg':msg})
        except:
            msg="Email Not Registerd"
            return render(request,'admin/login.html',{'msg':msg})
    else:           
        
        return render(request,'admin/login.html')
    
def logout(request):
        try:
            del request.session['email']
            del request.session['fname']
            del request.session['profile_picture']
            msg="User Logged Out successfully"
            return render(request,'admin/login.html')
        except:
            msg="User Logged Out successfully"
            return render(request,'admin/login.html')

def forgot_password(request):
    if request.method=="POST":
        try:
            user=User.objects.get(email=request.POST['email'])
            otp=random.randint(1000,9999)
            message="You OTP  For Forgot Password Is"+str(otp)
            send_mail("OTP For Forgot Password", message, settings.EMAIL_HOST_USER, [user.email,])
            request.session['email']=user.email
            request.session['otp']=otp
            return render(request,'otp.html')
        except:
            msg="Email is Not Registered"
            return render(request,'admin/forgot-password.html',{'msg':msg})
    else:
        return render(request,'admin/forgot-password.html')

def profile(request):
    user=User.objects.get(email=request.session['email'])
    if request.method=="POST":
        user.fname=request.POST['fname']
        user.lname=request.POST['lname']
        user.mobile=request.POST['mobile']
        user.address=request.POST['address']
        try:
            user.profile_picture=request.FILES['profile_picture']
        except:
            pass
        user.save()
        request.session['profile_picture']=user.profile_picture.url
        msg="Profile Updated Successfully"    
        return render(request,'admin/profile.html',{'user':user,'msg':msg})


    else:
        return render(request,'admin/profile.html',{'user':user})
