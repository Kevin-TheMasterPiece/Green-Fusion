from django import forms
from .models import empleado
class LoginForm(forms.Form):
    cedula = forms.IntegerField(label='Cédula')
    contrasena = forms.CharField(label='Contraseña', widget=forms.PasswordInput)

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = empleado
        fields = ['cedula', 'nom_emp', 'correo_emp', 'contrasena', 'tel_emp', 'direc_emp', 'ciudad_emp', 'foto_emp', 'FK_ID_Rol']
        
