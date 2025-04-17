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
from django.conf import settings
from django.conf.urls.static import static
from lawyer import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('lawindex', views.lawindex),
    path('viewcl', views.viewcl),
    path('viewcase', views.viewcase),
    path('adinst', views.adinst),
    path('maninst', views.maninst),
    path('mandoc', views.mandoc),
    path('viewfdbc', views.viewfdbc),
    # path('', views.login),
    # path('login1', views.login1),
    # path('forgotpass', views.forgotpass),
    # path('readmore/<int:id>', views.readmore),
    # path('logout', views.logout),
    path('editinst/<int:id>', views.editinst),
    path('delete1/<int:id>', views.delete1),
    # path('search', views.search),




] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

