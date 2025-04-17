from django.shortcuts import render, redirect
# from .models import attorneys, contactEnquiry
from client.models import Review1


# Create your views here.
# def loadfile(request):
#     return render(request, "guestuser/login1.html")


# def home(request):
#     data = attorneys.objects.all
#     return render(request, "guestuser/home.html",{"data": data})


# def loadindex(request):
#     data = attorneys.objects.all
#     data1 = Review1.objects.all
#     return render(request, "guestuser/home.html", {"data": data,"data1":data1})


# def about(request):
#     return render(request, "guestuser/about.html")


# def contact(request):
#     return render(request, "guestuser/contact.html")


# def saveEnquiry(request):
#     if request.POST:
#         name = request.POST['Yourname']
#         email = request.POST['Youremail']
#         phone = request.POST['Phonenumber']
#         message = request.POST['message']
#         obj = contactEnquiry(name=name, email=email, phone=phone, message=message)
#         obj.save()
#         return redirect('/contact')
#     return render(request, "guestuser/contact.html")


# def civil(request):
#     return render(request, "guestuser/civil.html")


# def business(request):
#     return render(request, "guestuser/business.html")


# def criminal(request):
#     return render(request, "guestuser/criminal.html")


# def family(request):
#     return render(request, "guestuser/family.html")


# def education(request):
#     return render(request, "guestuser/education.html")


# def cyber(request):
#     return render(request, "guestuser/cyber.html")


# def terms(request):
#     return render(request, "guestuser/terms-of-use.html")

# def jill(request):
#     return render(request, "guestuser/jillmehtaabout.html")

# def dhruvik(request):
#     return render(request, "guestuser/dhruvikpatelabout.html")

# def privacy(request):
#     return render(request, "guestuser/privacy.html")

# def help(request):
#     return render(request, "guestuser/help.html")

# def faq(request):
#     return render(request, "guestuser/faq.html")


# def readmore(request,id):
#     data=attorneys.objects.get(id=id)
#     return render(request,"guestuser/readmore.html",{"data":data})

