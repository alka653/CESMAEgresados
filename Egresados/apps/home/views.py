from django.views.generic import CreateView, ListView, TemplateView
from django.contrib.messages.views import SuccessMessageMixin
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from .forms import EgresadosForm
from .models import Egresados

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

class ListEgresados(ListView):
	template_name = 'Egresados_list.html'
	model = Egresados