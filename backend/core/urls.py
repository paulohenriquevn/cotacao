"""core URL Configuration """
from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from rest_framework_swagger.views import get_swagger_view
from cadastros_classificacao.urls import cadastros_classificacao_urls
from documento.urls import documento_urls
from core.api.views import UserList

schema_view = get_swagger_view(title='Gestão documental API')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('classificacao/',include(cadastros_classificacao_urls)),
    path('documento/',include(documento_urls)),
    path('usuarios/', UserList.as_view({'get': 'list'})),
    path('', schema_view)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
