from django.views.generic import CreateView, ListView, TemplateView
from django.contrib.messages.views import SuccessMessageMixin
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import FormMixin
from django.shortcuts import render
from .forms import EgresadosForm
from django.db.models import Q
from .models import Egresados
from .forms import *

"""
def Egresados_view(request):
	if request.method == 'POST':
		form = EgresadosForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('')
"""
class MessageView(TemplateView):
	template_name = 'message.html'

class CreateEgresados(SuccessMessageMixin, CreateView):
	template_name = 'Egresados_form.html'
	success_url = reverse_lazy('message')
	success_message = 'Registro creado exitosamente.'
	form_class = EgresadosForm

class ListEgresados(FormMixin, ListView):
	template_name = 'Egresados_list.html'
	form_class = EgresadoSearchForm
	model = Egresados

	def get_form_kwargs(self):
		kwargs = super(ListEgresados, self).get_form_kwargs()
		kwargs['buscar_por'] = self.request.GET.get('buscar_por')
		return kwargs

	def get_queryset(self):
		queryset = super(ListEgresados, self).get_queryset()
		if self.request.GET.get('buscar_por') is not None:
			find_by = self.request.GET.get('buscar_por')
			queryset = queryset.filter(Q(nombres__icontains = find_by) | Q(apellidos__icontains = find_by) | Q(promocion__icontains = find_by) | Q(telefono__icontains = find_by) | Q(direccion__icontains = find_by) | Q(correo_electronico__icontains = find_by) | Q(ultimos_estudios__icontains = find_by) | Q(lugar_ultimo_estudio__icontains = find_by))
		return queryset