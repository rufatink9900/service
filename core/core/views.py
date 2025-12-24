from django.shortcuts import render
from cars.models import Service

def index(request):
    return render(request, 'index.html')

def services(request):
    all_services = Service.objects.all()
    return render(request, 'services.html', {'services': all_services})