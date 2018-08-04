# from django.conf.urls.static import static
# from django.conf.urls import url
# from django.contrib import admin
from django.urls import path
# from django.conf import settings
from . import views

app_name="main"

urlpatterns = [
    path('test', views.test, name='test'),
    path('home', views.home, name='home'),
    path('upload', views.upload.as_view(), name='upload'),
    path('result', views.result, name='result'),
    path('check', views.check, name='check'),

]