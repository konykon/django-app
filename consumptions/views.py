from django.shortcuts import render
import django_filters.rest_framework
from consumptions.models import Product, Product_Category, Consumption
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from rest_framework import generics
from consumptions.serializers import ConsumptionSerializer
from django.http import HttpResponseRedirect
from consumptions.filters import ConsumptionFilter
from django.contrib import messages


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


# class ConsumptionListView(generic.ListView):
#     model = Consumption
#     paginate_by = 10
#     context_object_name = 'consumptions'
#     template_name = 'consumptions.html'
#     filter_backends = [django_filters.rest_framework.DjangoFilterBackend]

#     def get_queryset(self):
#         # return Consumption.objects.order_by('timestamp')
#         return Consumption.objects.filter(product__category__code__icontains='LL')

def filter_by_product_category(request):
    f = ConsumptionFilter(request.GET, queryset=Consumption.objects.all())
    return render(request, 'consumptions.html', {'filter': f})


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
    db_codes = {}
    p_list = Product_Category.objects.all().values_list('code')
    for i in range(0, len(p_list)):
        db_codes[p_list[i][0]] = p_list[i][0]

    if "POST" == request.method:
        csv_file = request.FILES["csv_file"]
        file_data = csv_file.read().decode("utf-8")
        lines = file_data.split("\n")
        for line in lines[1:]:
            fields = line.split(",")
            if len(fields) == 2:
                code = fields[0]
                name = fields[1]
                if fields[0] not in db_codes:
                    p_c = Product_Category(code=code, name=name).save()
        messages.success(request, 'Form submission successful')
    return render(request, "upload_product_categories_csv.html") 
