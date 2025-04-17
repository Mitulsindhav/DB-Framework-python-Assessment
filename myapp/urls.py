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
from django.contrib import admin
from django.urls import path
from myapp import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', views.loadindex),
    # path('loadfile', views.loadfile),
    # path('home', views.home),
    # path('about', views.about),
    # path('contact', views.contact),
    # path('saveEnquiry', views.saveEnquiry),
    # path('civil', views.civil),
    # path('criminal', views.criminal),
    # path('cyber', views.cyber),
    # path('family', views.family),
    # path('business', views.business),
    # path('education', views.education),
    # path('terms', views.terms),
    # path('jill', views.jill),
    # path('dhruvik', views.dhruvik),
    # path('privacy', views.privacy),
    # path('help', views.help),
    # path('faq', views.faq),
    # path('readmore/<int:id>', views.readmore),



] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
