from django import forms
from .models import reclamo, factura
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ReclamoForm(forms.ModelForm):
    class Meta:
        model = reclamo
        fields = ['des_recla', 'foto_reclamo']
        labels = {
            'des_recla': 'Descripción del reclamo',
            'foto_reclamo': 'Foto del reclamo',
        }

class CustomUserCreationForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
	def clean_email(self):
		email = self.cleaned_data['email']

		if User.objects.filter(email=email).exists():
			raise forms.ValidationError('Este correo electrónico ya está registrado')
		return email
              
class FacturaCreateForm(forms.ModelForm):
    class Meta:
        model = factura
        fields = ['nom_client', 'apell_client', 'direccion',
                  'city'] 
        labels = {
            'nom_client': 'Nombre',
            'apell_client': 'Apellido',
            'direccion': 'Direccion de envio',
            'city': 'ciudad'
        }           
    
	
	