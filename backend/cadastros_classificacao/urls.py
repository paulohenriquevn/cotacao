
from rest_framework.routers import DefaultRouter

from cadastros_classificacao.api.views import TipoDigitalizacaoView
from cadastros_classificacao.api.views import FrequenciaUsoView
from cadastros_classificacao.api.views import PrazosGuardaView
from cadastros_classificacao.api.views import FaseIntermediariaView
from cadastros_classificacao.api.views import DestinacaoFinalView
from cadastros_classificacao.api.views import GrauSigioDocumentacaoView

router = DefaultRouter()
router.register(r'tipodigitalizacao', TipoDigitalizacaoView)
router.register(r'frequenciauso', FrequenciaUsoView)
router.register(r'prazosguarda',PrazosGuardaView)
router.register(r'faseintermediaria',FaseIntermediariaView)
router.register(r'destinacaofinal',DestinacaoFinalView)
router.register(r'grausigiodocumentacao',GrauSigioDocumentacaoView)

cadastros_classificacao_urls = router.urls