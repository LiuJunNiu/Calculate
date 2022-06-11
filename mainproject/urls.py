"""mainproject URL Configuration

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
from firstWEB import views

urlpatterns = [
    path('admin', admin.site.urls),
    path('index', views.index),
    path('calPage', views.calPage),
    path('calucate', views.calucate),
    path('input_page', views.input_page),
    path('calculate_result', views.calculate_result),
    path('navigation', views.navigation),
    path('summary', views.summary),
    path('table1', views.table),
    path('barChart', views.bar_chart),
    # path('lineChart', views.line_chart),
    path('chart', views.chart),
    path('png1', views.img_show),

]
