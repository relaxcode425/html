#from django.conf.urls import url
from django.urls import path
from DondeLaFlaca import views

urlpatterns = [
    path('', views.Principal, name='Principal'),
]