from django import forms

from django.contrib.auth.models import User

class RegisterForm(forms.Form):
    
    username = forms.CharField(required=True,
                                min_length=4,
                                max_length=50,
                                widget=forms.TextInput(attrs={
                                    'class': 'form-control',
                                    'id': 'username',
                                }))
    
    email = forms.EmailField(required=True,
                             widget=forms.EmailInput(attrs={
                                    'class': 'form-control',
                                    'id': 'email',
                                    'placeholder': 'example@email.com'
                                }))
    
    password = forms.CharField(required=True,
                                widget=forms.PasswordInput(attrs={
                                    'class': 'form-control',
                                    'placeholder': 'password'
                                }))

    password2 = forms.CharField(label='Confirmar Password',
                                required=True,
                                widget=forms.PasswordInput(attrs={
                                   'class': 'form-control',
                                   'placeholder': 'password'
                               }))

    # con este metodo validamos el campo que queramos (usando clean_campo-a-validar)
    def clean_username(self):
        username = self.cleaned_data.get('username')

        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('El username ya esta siendo usado')
        
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('El email ya esta registrado')
        
        return email

    # esto solo se ultiliza si se quiere validar un campo y depende uno de otro.
    def clean(self):
        cleaned_data = super().clean()

        if cleaned_data.get('password2') != cleaned_data.get('password'):
            self.add_error('password2', 'el password no coincide') 

    def save(self):
       return User.objects.create_user(
           self.cleaned_data.get('username'),
           self.cleaned_data.get('email'),
           self.cleaned_data.get('password')
        )
        