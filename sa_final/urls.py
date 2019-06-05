"""sa_final URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from fa_system import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('index/',views.index),
    path('login/',views.login),
    path('login/action/',views.login_action),
    path('product/',views.product),
    path('about/',views.about),
    path('statusReport/',views.statusReport),
    path('branchReport/',views.branchReport),
    path('salesReport/',views.salesReport),
    path('financialReport/',views.financialReport),
    path('analyzeData/',views.analyzeData),
    path('upload/',views.upload),
    path('analyzeData/',views.analyzeData),
    path('analysisReport/',views.analysisReport),

]
