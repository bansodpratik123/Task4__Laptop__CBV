from django.shortcuts import render
from django.db import models
from .models import Laptops
from django.views import View 
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.



# Create your views here.

class LaptopListView(ListView):
    model = Laptops


class LaptopCreateView(CreateView):
    model = Laptops
    fields = '__all__'
    success_url = '/show/'


class LaptopUpdateView(UpdateView):
    model = Laptops
    fields = '__all__'
    success_url = '/show/'


class LaptopDeleteView(DeleteView):
    model = Laptops
    success_url = '/show/'


def homeview(request):
    template_name='home.html'
    context={}
    return render(request,template_name,context)