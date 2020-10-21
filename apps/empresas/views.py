from django.views.generic.edit import CreateView, UpdateView
from .models import Empresa


class EmpresaCreate (CreateView):
    model = Empresa
    fields = ['nome']


    def form_valid(self, form):
        obj = form.save()
        funcionario = self.request.user.funcionario
        funcionario.empresa = obj
        funcionario.save()


class EmpresaEdit(UpdateView):
    model = Empresa
    fields = ['nome']





