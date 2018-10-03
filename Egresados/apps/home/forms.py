from django import forms

from .models import Egresados


class EgresadosForm(forms.ModelForm):

	class Meta:
		model = Egresados
		fields = '__all__'

		labels = {
			'nombres': 'Nombres:',
			'apellidos': 'Apellidos:',
			'promocion': 'Promocion:',
			'telefono': 'Telefono:',
			'direccion': 'Direccion:',
			'correo_electronico': 'Correo electronico:',
			'ultimos_estudios': 'Ultimos estudios:',
			'lugar_ultimo_estudio': 'Lugar ultimo estudio:'
		}
		widgets = {
			'nombres': forms.TextInput(attrs={'class':'form-control', 'required': True}),
			'apellidos': forms.TextInput(attrs={'class':'form-control', 'required': True}),
			'promocion': forms.TextInput(attrs={'class':'form-control only-number', 'required': True}),
			'telefono': forms.TextInput(attrs={'class':'form-control only-number', 'required': True}),
			'direccion': forms.TextInput(attrs={'class':'form-control', 'required': True}),
			'correo_electronico': forms.EmailInput(attrs={'class':'form-control', 'required': True}),
			'ultimos_estudios': forms.TextInput(attrs={'class':'form-control', 'required': True}),
			'lugar_ultimo_estudio': forms.TextInput(attrs={'class':'form-control', 'required': True}),
		}

class EgresadoSearchForm(forms.Form):
	buscar_por = forms.CharField(label = 'Buscar por:', widget = forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'Digite palabra a buscar'}))

	def __init__(self, *args, **kwargs):
		buscar_por = kwargs.pop('buscar_por', None)
		super(EgresadoSearchForm, self).__init__(*args, **kwargs)
		if buscar_por: self.fields['buscar_por'].initial = buscar_por