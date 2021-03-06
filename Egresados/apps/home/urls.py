from django.contrib.auth.decorators import login_required
from django.conf.urls import url, patterns
from .views import *

urlpatterns = patterns('Egresados.apps.home.views',
	url(r'^$', CreateEgresados.as_view(), name = 'crear_egresados'),
	url(r'^message/$', MessageView.as_view(), name = 'message'),
	url(r'^lista/$', login_required(ListEgresados.as_view()), name = 'lista_egresados'),
	url(r'^egresado/(?P<numero_documento>\d+)/$', UpdateEgresados.as_view(), name = 'actualizar_egresado'),
	url(r'^listado/$', ImprimirListado.as_view(), name = 'listado_egresado')
)