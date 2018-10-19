from django.views.generic import CreateView, ListView, TemplateView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from django.core.urlresolvers import reverse_lazy, reverse
from django.views.generic.edit import FormMixin
from easy_pdf.views import PDFTemplateView
from django.contrib import messages
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

	def get_context_data(self, **kwargs):
		context = super(CreateEgresados, self).get_context_data(**kwargs)
		context['url'] = reverse_lazy('crear_egresados')
		context['title_form'] = '¿Eres egresado? Ingresa los siguientes datos'
		return context

	def form_valid(self, form):
		obj = form.save(commit = False)
		if Egresados.objects.filter(numero_documento = obj.numero_documento).count() > 0:
			messages.warning(self.request, 'Parece que ya estas registrado en la base de datos. Puedes <a href="'+reverse('actualizar_egresado', kwargs = {'numero_documento': obj.numero_documento})+'">Actualizar datos</a>')
			return super(CreateEgresados, self).form_invalid(form)
		return super(CreateEgresados, self).form_valid(form)

class UpdateEgresados(SuccessMessageMixin, UpdateView):
	model = Egresados
	template_name = 'Egresados_form.html'
	success_url = reverse_lazy('message')
	success_message = 'Datos actualizados correctamente'
	form_class = EgresadosForm

	def get_context_data(self, **kwargs):
		context = super(UpdateEgresados, self).get_context_data(**kwargs)
		context['url'] = reverse('actualizar_egresado', kwargs = {'numero_documento': self.kwargs['numero_documento']})
		context['title_form'] = 'Actualiza tus datos'
		return context

	def get_object(self):
		return Egresados.objects.get(numero_documento = self.kwargs['numero_documento'])

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
			queryset = queryset.filter(Q(numero_documento__icontains = find_by) | Q(nombres__icontains = find_by) | Q(apellidos__icontains = find_by) | Q(promocion__icontains = find_by) | Q(telefono__icontains = find_by) | Q(direccion__icontains = find_by) | Q(correo_electronico__icontains = find_by) | Q(ultimos_estudios__icontains = find_by) | Q(lugar_ultimo_estudio__icontains = find_by))
		return queryset

class ImprimirListado(PDFTemplateView):
	template_name = "pdf.html"

	def get_context_data(self, **kwargs):
		context = super(ImprimirListado, self).get_context_data(**kwargs)
		context['query'] = Egresados.objects.all()
		return context