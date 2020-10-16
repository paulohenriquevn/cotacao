
from rest_framework.routers import DefaultRouter

from documento.api.views import DocumentoView

router = DefaultRouter()
router.register(r'documento', DocumentoView)

documento_urls = router.urls