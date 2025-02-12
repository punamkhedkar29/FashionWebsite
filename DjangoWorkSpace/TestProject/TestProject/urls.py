"""
URL configuration for TestProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from testApp import views
from testApp.views import contact
from testApp.views import index
from testApp.views import success
from testApp.views import signup
from testApp.views import product
from testApp.views import collection
from testApp.views import blog
from testApp.views import signin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('index.html', index, name='index'),
    path('contact/', contact, name='contact'),
    path('success/', success, name='success'),
    path('signup/', signup, name='signup'),
    path('signin/', signin, name='signin'),
    path('product.html', product, name='product'),
    path('blog.html', blog, name='blog'),
    path('collection.html', collection, name='collection'),

]
