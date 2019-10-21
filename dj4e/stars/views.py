from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.template.loader import render_to_string

from stars.models import Star, Type
from stars.forms import TypeForm

class StarList(LoginRequiredMixin, View) :
    def get(self, request):
        tc = Type.objects.all().count();
        sl = Star.objects.all();
        ctx = { 'type_count': tc, 'star_list': sl };
        return render(request, 'stars/star_list.html', ctx)

class StarCreate(LoginRequiredMixin,CreateView):
    model = Star
    fields = '__all__'
    success_url = reverse_lazy('stars:all')

class StarUpdate(LoginRequiredMixin, UpdateView):
    model = Star
    fields = '__all__'
    success_url = reverse_lazy('stars:all')

class StarDelete(LoginRequiredMixin, DeleteView):
    model = Star
    fields = '__all__'
    success_url = reverse_lazy('stars:all')

class TypeView(LoginRequiredMixin, View) :
    def get(self, request):
        tl = Type.objects.all();
        ctx = { 'type_list': tl };
        return render(request, 'stars/type_list.html', ctx)

class TypeCreate(LoginRequiredMixin, CreateView):
    model = Type
    fields = '__all__'
    success_url = reverse_lazy('stars:all')

class TypeUpdate(LoginRequiredMixin, UpdateView):
    model = Type
    fields = '__all__'
    success_url = reverse_lazy('stars:all')

class TypeDelete(LoginRequiredMixin, DeleteView):
    model = Type
    fields = '__all__'
    success_url = reverse_lazy('stars:all')