from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UsuarioForm(UserCreationForm):
    # posso colocar alguns campos para serem obrigatorios no cadastro de novos usuarios
    # email = forms.EmailField(max_lengeth=100)
    class Meta:
        model = User
        fields = ['username']

