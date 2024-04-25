from django import forms

class LoginForm(forms.Form):
    cedula = forms.IntegerField(label='Cédula')
    contrasena = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
