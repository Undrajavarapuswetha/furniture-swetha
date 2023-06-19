"""Furni_1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from user import views as v
from admins import views as v1
from django.conf import settings
from django.conf.urls.static import static


app_name='user'

urlpatterns = [
       path('admin/', admin.site.urls),
       path('',v1.HOME,name='HOME'),
       path('index/',v.index, name='index'),
       path('login/',v.login,name='login'),
       path('reg/', v.reg, name='reg'),
       path('home/',v.home,name='home'),
       path('profile/',v.profile,name='profile'),
       path('alogin/',v1.alogin,name='alogin'),
       path('ahome/',v1.ahome,name='ahome'),
       path('addproduct/',v1.addproduct,name='addproduct'),
       path('viewproduct/',v1.viewproduct,name='viewproduct'),
       path('profile1/',v1.profile1,name='profile1'),
       path('products/',v.products,name='products'),
       path('products/<int:id>/',v.products,name='products'),
       path('buyproduct',v.buyproduct,name='buyproduct'),
       path('buyproduct/<int:id>/buy',v.buyproduct, name='buyproduct'),
       path('purchase/',v.purchase,name='purchase'),
       path('lastview/',v.lastview,name='lastview'),
       path('logout/',v.logout,name='logout'),
       path('alogout/',v1.alogout,name='alogout'),
       path('alastview',v1.alastview,name='alastview'),
       path('categories/', v.categories, name='categories'),
       path('contact/', v.contact, name='contact'),
       path('bed/', v.bed, name='bed'),
       path('chair/', v.chair, name='chair'),
       path('swing/', v.swing, name='swing'),
       path('sofa/',v.sofa,name='sofa'),
       path('end/',v.end,name='end'),








]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL ,document_root=settings.MEDIA_ROOT)
































