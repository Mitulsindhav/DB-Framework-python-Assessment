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
from superuser import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', views.home),
                  path('court1', views.court1),
                  path('lawyer1', views.lawyer1),
                  path('client1', views.client1),
                  path('feedback', views.feedback),
                  path('case1', views.case1),
                  path('category1', views.category1),
                  path('manlaw', views.manlaw),
                  path('edit1/<int:id>', views.edit1),
                  path('delete1/<int:id>', views.delete1),
                  path('edit2/<int:id>', views.edit2),
                  path('delete2/<int:id>', views.delete2),
                  path('edit3/<int:id>', views.edit3),
                  path('delete3/<int:id>', views.delete3),
                  path('edit4/<int:id>', views.edit4),
                  path('delete4/<int:id>', views.delete4),
                  path('mancase', views.mancase),
                  path('manclient', views.manclient),
                  path('mancategory', views.mancategory),
                  path('maninstruction', views.maninstruction),
                  path('manpayment', views.manpayment),
                  path('manappointment', views.manappointment),
                  path('user', views.user),
                  path('search1', views.search1),
                  path('search2', views.search2),
                  path('search3', views.search3),
                  path('search4', views.search4),
                  path('forgotlawyer', views.forgotlawyer),
                  path('forgotclient', views.forgotclient),
                  path('notification', views.notification),
                  path('register/', views.register,name='register'),
                  path('login/', views.login,name='login'),

                  path('profile/', views.profile,name='profile'),
                  path('logout/', views.logout,name='logout'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
