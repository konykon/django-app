from django.shortcuts import render
from consumptions.models import Product, Product_Category, Consumption
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from rest_framework import generics
from consumptions.serializers import ConsumptionSerializer

# Create your views here.

def index(request):
    return render(request, 'index.html')

def base(request):
    return render(request, 'base.html')

class ConsumptionCreateApi(generics.CreateAPIView):
    queryset = Consumption.objects.all()
    serializer_class = ConsumptionSerializer

class ConsumptionApi(generics.ListAPIView):
    queryset = Consumption.objects.all()
    serializer_class = ConsumptionSerializer

class ConsumptionUpdateApi(generics.RetrieveUpdateAPIView):
    queryset = Consumption.objects.all()
    serializer_class = ConsumptionSerializer

class ConsumptionDeleteApi(generics.DestroyAPIView):
    queryset = Consumption.objects.all()
    serializer_class = ConsumptionSerializer

class ConsumptionListView(generic.ListView):
    model = Consumption
    paginate_by = 10
    context_object_name = 'consumption_list'
    template_name = 'consumption_list.html'

class ConsumptionCreate(CreateView):
    model = Consumption
    fields = ['product', 'quantity']
    template_name = 'consumption_form.html'
    success_url = reverse_lazy('consumptions')

class ConsumptionUpdate(UpdateView):
    model = Consumption
    fields = '__all__'
    template_name = 'consumption_form.html'
    success_url = reverse_lazy('consumptions')
    
class ConsumptionDelete(DeleteView):
    model = Consumption
    template_name = 'consumption_confirm_delete.html'
    success_url = reverse_lazy('consumptions')
