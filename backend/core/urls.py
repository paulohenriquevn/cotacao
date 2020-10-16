"""core URL Configuration """
from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from rest_framework_swagger.views import get_swagger_view
from cadastros_classificacao.urls import cadastros_classificacao_urls
from documento.urls import documento_urls

schema_view = get_swagger_view(title='Gestão documental API')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('classificacao/',include(cadastros_classificacao_urls)),
    path('documento/',include(documento_urls)),
    path('', schema_view)
]
