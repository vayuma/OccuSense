from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('page2', views.data, name='page'),
    path('page2', views.data, name='data')
]