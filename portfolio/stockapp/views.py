from django.shortcuts import render
from .models import Stock

# Create your views here.
def home(request):
    stock_data = Stock.objects.all()


    return render(request, 'home.html', {"stock": stock_data})

def testimonials(request):
    return render(request, 'testimonials.html', {})