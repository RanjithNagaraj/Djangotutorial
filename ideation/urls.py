from django.urls import path

from . import views

urlpatterns = [

    path('classify', views.classify, name='classify'),
    path('dump', views.dumpclassify, name='dumpclassify'),
    path('recommend', views.recommending, name='recommend')
]