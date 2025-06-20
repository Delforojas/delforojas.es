"""
URL configuration for webpersonal project.

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
from core import views as core_views
from portfolio import views as portfolio_views
from formacion import views as formacion_views
from formacion import views as experiencia_academica_views
from laboral import views as experiencia_laboral_views
from dataset import views as dataset_views

from django.conf import settings

urlpatterns = [
    path('', core_views.home, name="home"),
    path('about-me/', core_views.about, name="about"),
    path('portfolio/', portfolio_views.portfolio, name="portfolio"),
    path('dataset/', dataset_views.dataset, name='dataset'),
    path('formacion/', formacion_views.formacion, name="formacion"),
    path('experiencia/', experiencia_academica_views.experiencia, name='experiencia'),
    path('experiencialaboral/', experiencia_laboral_views.experiencia_laboral, name='experiencialaboral'),
    path('contact/', core_views.contact, name="contact"),
    path('admin/', admin.site.urls),
] 

