from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views import generic
from .models import Proyecto,tipo_proyecto,curso
from extra_views import CreateWithInlinesView, UpdateWithInlinesView, InlineFormSetFactory

# Productos views

class ProyectoListView(generic.ListView):
    model = Proyecto
    template_name = "list.html"


class ProyectoDetailView(generic.DetailView):
    model = Proyecto
    template_name = "detail.html"

class ProyectoCreateView(generic.CreateView):
    model = Proyecto
    fields = '__all__'
    template_name = "form.html"


class ProyectoUpdateView(generic.UpdateView):
    model = Proyecto
    fields = '__all__'
    template_name = "form.html"

class ProyectoDeleteView(generic.DeleteView):
    model = Proyecto
    template_name = "delete.html"
    success_url = reverse_lazy('proyectos:index')

