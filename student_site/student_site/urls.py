"""student_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from studentapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('firstyear/',views.firstyear,name='firstyear'),
    path('secondyear/',views.secondyear,name='secondyear'),
    path('Biotech/',views.Biotech,name='Biotech'),
    path('CS/',views.Biotech,name='CS'),
    path('civil/',views.civil,name='civil'),
    path('Chemical/',views.Chemical,name='Chemical'),
    path('EandIn/',views.EandIn,name='EandIn'),
    path('electrical/',views.electrical,name='electrical'),
    path('Eandcomm/',views.Eandcomm,name='Eandcomm'),
    path('Eandcomp/',views.Eandcomp,name='Eandcomp'),
    path('Mechanical/',views.Mechanical,name='Mechanical'),
    path('Mechatronics/',views.Mechatronics,name='Mechatronics'),
    path('Production/',views.Production,name='Production'),
    path('c/',views.c,name='c'),
    path('cpp/',views.cpp,name='c++'),
    path('chem/',views.chem,name='chem'),
    path('ed/',views.ed,name='ed'),
    path('electrical1/',views.electrical1,name='electrical1'),
    path('electronics/',views.electronics,name='electronics'),
    path('engDesign1/',views.engDesign1,name='engDesign1'),
    path('environment/',views.environment,name='environment'),
    path('maths/',views.maths,name='maths'),
    path('maths2/',views.maths2,name='maths2'),
    path('mechanics/',views.mechanics,name='mechanics'),
    path('physics/',views.physics,name='physics'),
    path('proffComm/',views.proffComm,name='proffComm'),

]

urlpatterns += staticfiles_urlpatterns()
