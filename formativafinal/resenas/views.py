from typing import Any
from django.db import models
from django.shortcuts import render
from django.views.generic import CreateView, ListView, DeleteView, UpdateView
from .models import Resena
from django.urls import reverse_lazy
from .forms import ResenaForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class ResenaListView(ListView):
    model = Resena
    template_name = 'resenas/resenaList.html'
    context_object_name = 'resenas'

@method_decorator(login_required, name='dispatch')
class ResenaCreateView(CreateView):
    model = Resena
    template_name = 'resenas/ResenasForm.html'
    form_class = ResenaForm
    success_url = reverse_lazy('list')

@method_decorator(login_required, name='dispatch')
class ResenaDeleteView(DeleteView):
    model = Resena
    template_name = 'resenas/resenaDelete.html'
    success_url = reverse_lazy('list')

    def get_object(self, queryset=None):
            obj = super().get_object(queryset=queryset)
            return obj

@method_decorator(login_required, name='dispatch')
class ResenaUpdateView(UpdateView):
    model = Resena
    template_name = 'resenas/resenaUpdate.html'
    form_class = ResenaForm
    success_url = reverse_lazy('list')

    def get_object(self, queryset=None):
            obj = super().get_object(queryset=queryset)
            return obj