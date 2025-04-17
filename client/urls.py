"""webapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from  django.contrib import admin
from django.urls import path
from client import views
from .views import upload_document
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [

                #   path('', views.login),
                #   path('login2', views.login2),
                #   path('logout1', views.logout1),
                #   path('Feedback', views.Feedback),
                #   path('forpass', views.forpass),
                #   path('dashboardc', views.dashboardc),
                #   path('case1', views.case1),
                #   path('instruction', views.instruction),
                #   path("home", views.home, name="home"),
                #   path("payment", views.order_payment, name="payment"),
                #   path("callback", views.callback, name="callback"),
                #   path("dele/<int:id>", views.dele),
                #   path('upload_document', upload_document, name='upload_document'),






              ] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
