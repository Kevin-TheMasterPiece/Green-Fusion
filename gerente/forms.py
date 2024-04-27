from django import forms
from .models import empleado
class LoginForm(forms.Form):
    cedula = forms.IntegerField(label='Cédula')
    contrasena = forms.CharField(label='Contraseña', widget=forms.PasswordInput)

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = empleado
        fields = ['cedula', 'nom_emp', 'correo_emp', 'contrasena', 'tel_emp', 'direc_emp', 'ciudad_emp', 'foto_emp', 'FK_ID_Rol']
        widgets = {
            'cedula': forms.TextInput(attrs={'class': 'form-control'}),
            'nom_emp': forms.TextInput(attrs={'class': 'form-control'}),
            'correo_emp': forms.EmailInput(attrs={'class': 'form-control'}),
            'contrasena': forms.TextInput(attrs={'class': 'form-control'}),
            'tel_emp': forms.TextInput(attrs={'class': 'form-control'}),
            'direc_emp': forms.TextInput(attrs={'class': 'form-control'}),
            'ciudad_emp': forms.TextInput(attrs={'class': 'form-control'}),
            'foto_emp': forms.FileInput(attrs={'class': 'form-control'}),
            'FK_ID_Rol': forms.HiddenInput(attrs={'value': '1'}),  # Si deseas mantener este campo oculto
        }
