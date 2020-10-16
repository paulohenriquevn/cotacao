"""core URL Configuration """
from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from rest_framework import routers
from cadastros_classificacao.urls import cadastros_classificacao_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('classificacao/',include(cadastros_classificacao_urls))
]
