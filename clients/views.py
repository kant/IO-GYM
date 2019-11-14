from django.shortcuts import render

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import *
from clients.forms import *

from django.urls import reverse
from django.shortcuts import redirect

from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

from django import forms
from .filters import *

class MembershipList(ListView):
    model=MEMBERSHIPS

class MembershipDelete(SuccessMessageMixin, DeleteView):
    model = MEMBERSHIPS
    form = MEMBERSHIPS
    fields = "__all__"

    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self):
        success_message = 'Entrenador Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre
        messages.success (self.request, (success_message))
        return reverse('index membership') # Redireccionamos a la vista principal 'leer'

class MembershipDetails(DetailView):
    model=MEMBERSHIPS

class MembershipEdit(SuccessMessageMixin,UpdateView):
    form_class = MembershipForm
    model = MEMBERSHIPS
    success_message = 'Cliente Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre

    # Redireccionamos a la página principal luego de actualizar un registro o postre
    def get_success_url(self):
        return reverse('index membership') # Redireccionamos a la vista principal 'leer'

class MembershipCreate(SuccessMessageMixin,CreateView):
    form_class = MembershipForm
    model = MEMBERSHIPS
    success_message = 'Entrenador Creado Correctamente !' # Mostramos este Mensaje luego de Crear un Postre

    # Redireccionamos a la página principal luego de crear un registro o postre
    def form_valid(self, form):
        data = form.save()  # save form
        return redirect('edit membership', pk=data.membership_id)

class GymClassesList(ListView):
    model=GYMCLASSES

class GymClassesDelete(SuccessMessageMixin, DeleteView):
    model = GYMCLASSES
    form = GYMCLASSES
    fields = "__all__"

    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self):
        success_message = 'Entrenador Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre
        messages.success (self.request, (success_message))
        return reverse('index gymclasses') # Redireccionamos a la vista principal 'leer'


class GymClassesEdit(SuccessMessageMixin, UpdateView):
    model = GYMCLASSES
    form = GYMCLASSES
    fields = "__all__"
    success_message = 'Cliente Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre

    # Redireccionamos a la página principal luego de actualizar un registro o postre
    def get_success_url(self):
        return reverse('index gymclases') # Redireccionamos a la vista principal 'leer'

class GymClassesDetail(DetailView):
    model=GYMCLASSES

class GymClassesCreate(SuccessMessageMixin, CreateView):
    model = GYMCLASSES
    form = GYMCLASSES
    fields = "__all__"
    success_message = 'Entrenador Creado Correctamente !' # Mostramos este Mensaje luego de Crear un Postre

    # Redireccionamos a la página principal luego de crear un registro o postre
    def get_success_url(self):
        return reverse('index gymclasses') # Redireccionamos a la vista principal 'leer'

class GroupsList(ListView):
    model=GROUPS

class GroupsDelete(SuccessMessageMixin, DeleteView):
    model = GROUPS
    form = GROUPS
    fields = "__all__"

    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self):
        success_message = 'Entrenador Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre
        messages.success (self.request, (success_message))
        return reverse('index groups') # Redireccionamos a la vista principal 'leer'


class GroupsEdit(SuccessMessageMixin, UpdateView):
    model = GROUPS
    form = GROUPS
    fields = "__all__"
    success_message = 'Cliente Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre

    # Redireccionamos a la página principal luego de actualizar un registro o postre
    def get_success_url(self):
        return reverse('index groups') # Redireccionamos a la vista principal 'leer'

class GroupsDetail(DetailView):
    model=GROUPS

class GroupsCreate(SuccessMessageMixin, CreateView):
    model = GROUPS
    form = GROUPS
    fields = "__all__"
    success_message = 'Entrenador Creado Correctamente !' # Mostramos este Mensaje luego de Crear un Postre

    # Redireccionamos a la página principal luego de crear un registro o postre
    def get_success_url(self):
        return reverse('index groups') # Redireccionamos a la vista principal 'leer'


class hoursCreate(SuccessMessageMixin, CreateView):
    model = HOURS
    form = HOURS
    fields = "__all__"
    success_message = 'Creado Correctamente !' # Mostramos este Mensaje luego de Crear un Postre

    # Redireccionamos a la página principal luego de crear un registro o postre
    def get_success_url(self):
        return reverse('index hours') # Redireccionamos a la vista principal 'leer'

class hoursDelete(SuccessMessageMixin, DeleteView):
    model = HOURS
    form = HOURS
    fields = "__all__"

    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self):
        success_message = 'Entrenador Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre
        messages.success (self.request, (success_message))
        return reverse('index hours') # Redireccionamos a la vista principal 'leer'

class hoursView(ListView):
    model= HOURS

class weekdaysCreate(SuccessMessageMixin, CreateView):
    model = WEEKDAYS
    form = WEEKDAYS
    fields = "__all__"
    success_message = 'Creado Correctamente !' # Mostramos este Mensaje luego de Crear un Postre

    # Redireccionamos a la página principal luego de crear un registro o postre
    def get_success_url(self):
        return reverse('index weekdays') # Redireccionamos a la vista principal 'leer'

class weekdayDelete(SuccessMessageMixin, DeleteView):
    model = WEEKDAYS
    form = WEEKDAYS
    fields = "__all__"

    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self):
        success_message = 'Entrenador Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre
        messages.success (self.request, (success_message))
        return reverse('index weekdays') # Redireccionamos a la vista principal 'leer'

class weekdaysView(ListView):
    model= WEEKDAYS

class clientsView(ListView):
    model=clientesView

class trainersAsistencia(SuccessMessageMixin, CreateView):
    model=TRAINERS_ATTENDANCES
    form=TRAINERS_ATTENDANCES
    fields = "__all__"
    Success_message='Ingreso exitoso'
    def get_success_url(self):
        return reverse('index')

class trainersAdministrar(ListView):
    model=TRAINERS

class trainersEliminar(SuccessMessageMixin, DeleteView):
    model = TRAINERS
    form = TRAINERS
    fields = "__all__"

    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self):
        success_message = 'Entrenador Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre
        messages.success (self.request, (success_message))
        return reverse('trainer administrar') # Redireccionamos a la vista principal 'leer'


class trainersEditar(SuccessMessageMixin, UpdateView):
    model = TRAINERS
    form = TRAINERS
    fields = "__all__"
    success_message = 'Cliente Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre

    # Redireccionamos a la página principal luego de actualizar un registro o postre
    def get_success_url(self):
        return reverse('trainer administrar') # Redireccionamos a la vista principal 'leer'

class trainersConsulta(DetailView):
    model=TRAINERS

class trainersRegistrar(SuccessMessageMixin, CreateView):
    model = TRAINERS
    form = TRAINERS
    fields = "__all__"
    success_message = 'Entrenador Creado Correctamente !' # Mostramos este Mensaje luego de Crear un Postre

    # Redireccionamos a la página principal luego de crear un registro o postre
    def get_success_url(self):
        return reverse('trainer administrar') # Redireccionamos a la vista principal 'leer'

class clientsAttendancesCrear(SuccessMessageMixin, CreateView):
    model=CLIENTS_ATTENDANCES
    form=CLIENTS_ATTENDANCES
    fields = "__all__"
    Success_message='Ingreso exitoso'
    def get_success_url(self):
        return reverse('index')

class clientsListado(ListView):
    model = CLIENTS

class clientsDetalle(DetailView):
    model = CLIENTS

class clientsCrear(SuccessMessageMixin, CreateView):
    model = CLIENTS
    form = CLIENTS
    fields = "__all__"
    success_message = 'Cliente Creado Correctamente !' # Mostramos este Mensaje luego de Crear un Postre

    # Redireccionamos a la página principal luego de crear un registro o postre

    def form_valid(self, form):
        data = form.save()  # save form
        membership=MEMBERSHIPS(client_id=CLIENTS(client_id=data.client_id))
        membership.save()
        return redirect('edit membership', pk=membership.membership_id)

class clientsActualizar(SuccessMessageMixin, UpdateView):
    model = CLIENTS
    form = CLIENTS
    fields = "__all__"
    success_message = 'Cliente Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre

    # Redireccionamos a la página principal luego de actualizar un registro o postre
    def get_success_url(self):
        return reverse('leer') # Redireccionamos a la vista principal 'leer'

class clientsEliminar(SuccessMessageMixin, DeleteView):
    model = CLIENTS
    form = CLIENTS
    fields = "__all__"

    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self):
        success_message = 'Cliente Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre
        messages.success (self.request, (success_message))
        return reverse('leer') # Redireccionamos a la vista principal 'leer'
