from django.shortcuts import render
import django_filters.rest_framework
from consumptions.models import Product, Product_Category, Consumption
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from rest_framework import generics
from consumptions.serializers import ConsumptionSerializer
from django.http import HttpResponseRedirect
from consumptions.forms import ProductsForm
import logging
from itertools import islice

# Create your views here.


def index(request):
    return render(request, 'index.html')


# Api crud
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

# UI crud


class ConsumptionListView(generic.ListView):
    model = Consumption
    paginate_by = 10
    context_object_name = 'consumption_list'
    template_name = 'consumption_list.html'
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]

    def get_queryset(self):
        return Consumption.objects.filter(product__category__code__icontains='LL')

    def filter_by_product_category(self):
        return Consumption.objects.filter(product__category__code__icontains='LL')


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


def upload_product_categories_csv(request):
    product_fields = Product._meta.local_fields
    if "POST" == request.method:
        csv_file = request.FILES["csv_file"]
        file_data = csv_file.read().decode("utf-8")
        lines = file_data.split("\n")
        for line in lines[1:]:
            fields = line.split(",")
            if len(fields) == 2:
                code = fields[0]
                name = fields[1]
                p_c = Product_Category(code=code, name=name).save()
    return render(request, "upload_product_categories_csv.html") 
