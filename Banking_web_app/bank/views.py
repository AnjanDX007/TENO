from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import User
# Create your views here.

def home(request):
    return render(request,'home.html')

class user_listview(ListView):
    model=User
    template_name = 'listview.html'

class user_detailview(DetailView):
    model=User
    template_name = 'detailview.html'
    context_object_name = 'cust'