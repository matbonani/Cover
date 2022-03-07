from django.views.generic.edit import CreateView
from .forms import UsuarioForm
from django.urls import reverse_lazy


class UsuarioCreate(CreateView):
    template_name = 'createuser.html'
    form_class = UsuarioForm
    success_url = reverse_lazy('login')





