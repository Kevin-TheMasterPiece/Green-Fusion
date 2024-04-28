from django import forms
from gerente.models import empleado
from .models import proveedor
class PreparadorForm(forms.ModelForm):
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
            'FK_ID_Rol': forms.HiddenInput(attrs={'value': '2'}),  # Si deseas mantener este campo oculto
        }
class ProveedorForm(forms.ModelForm):
    class Meta:
        model = proveedor
        fields = ['nit', 'nom_prov', 'correo_prov', 'tel_prov', 'ciudad_prov', 'desc_prov']
        widgets = {
            'nit': forms.TextInput(attrs={'class': 'form-control'}),
            'nom_prov': forms.TextInput(attrs={'class': 'form-control'}),
            'correo_prov': forms.EmailInput(attrs={'class': 'form-control'}),
            'tel_prov': forms.TextInput(attrs={'class': 'form-control'}),
            'ciudad_prov': forms.TextInput(attrs={'class': 'form-control'}),
            'desc_prov': forms.TextInput(attrs={'class': 'form-control'}),

        }
