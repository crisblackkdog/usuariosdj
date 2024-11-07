from django import forms
#
from .models import User
from django.contrib.auth import authenticate
class UserRegisterForm(forms.ModelForm):
    
    password =forms.CharField(
        label= 'Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Contraseña'
            }
        )
    )
    password2 =forms.CharField(
        label= 'Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Repetir Contraseña'
            }
        )
    )

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'nombres',
            'apellidos',
            'genero',
        )

    def clean_password2(self):
        password = self.cleaned_data['password']
        password2 = self.cleaned_data['password2']

        if len(password) < 8 :
            self.add_error('password', 'debe ser meno a 8 caracteres')

        elif password != password2:
            self.add_error('password2', 'no son iguales')


class LoginForm(forms.Form):
    username =forms.CharField(
        label= 'username',
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder':'Usuario'
            }
        )
    )
    password =forms.CharField(
        label= 'Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Contraseña'
            }
        )
    )
    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        username = self.cleaned_data['username']
        password= self.cleaned_data['password']

        if not authenticate(username=username, password= password):
            raise forms.ValidationError('Los datos de usuarios no son correctos')
        
        return self.cleaned_data
    
class UpdatePasswordForm(forms.Form):
    password = forms.CharField(
        label= 'Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'contraseña actual'
            }
        )
    )
    password2 = forms.CharField(
        label= 'Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Contraseña Nueva'
            }
        )
    )

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')

        # Validación de longitud
        if password and len(password) < 8:
            self.add_error('password', 'La contraseña debe tener al menos 8 caracteres.')

        # Validación de contraseñas iguales
        if password and password == password2:
            self.add_error('password2', 'La nueva contraseña no debe ser igual a la contraseña actual.')

        return cleaned_data

class VerificationForm(forms.Form):
    codregistro = forms.CharField(required=True)