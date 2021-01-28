from django.shortcuts import render

from consumptions.models import Product, Product_Category, Consumption
from consumptions.serializers import ConsumptionSerializer
from consumptions.filters import ConsumptionFilter

from rest_framework import viewsets

from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from django_filters.views import FilterView


class ConsumptionViewSet(viewsets.ModelViewSet):
    """Consumption REST API ViewSet, includes Create, Update, Delete"""
    queryset = Consumption.objects.all()
    serializer_class = ConsumptionSerializer


class Index(View):
    template_name = 'index.html'

    def get(self, request):
        return render(request, self.template_name)


class ConsumptionList(FilterView):
    """Consumption list with option to filter by product category"""
    model = Consumption
    context_object_name = 'consumptions'
    template_name = 'consumption_list.html'
    filterset_class = ConsumptionFilter


class ConsumptionCreate(CreateView):
    model = Consumption
    fields = ['product', 'quantity']
    template_name = 'consumption_form.html'
    success_url = reverse_lazy('consumptions:consumption_list')


class ConsumptionUpdate(UpdateView):
    model = Consumption
    fields = '__all__'
    template_name = 'consumption_form.html'
    success_url = reverse_lazy('consumptions:consumption_list')


class ConsumptionDelete(DeleteView):
    model = Consumption
    template_name = 'consumption_confirm_delete.html'
    success_url = reverse_lazy('consumptions:consumption_list')


def upload_csv(request):
    db_codes = {}
    p_list = Product_Category.objects.all().values_list('code')
    for i in range(0, len(p_list)):
        db_codes[p_list[i][0]] = p_list[i][0]

    if request.method == "POST":
        csv_file = request.FILES["csv_file"]

        if not csv_file.name.endswith('.csv'):
            messages.error(request, 'This is not a csv file')
        else:
            file_data = csv_file.read().decode("utf-8")
            lines = file_data.split("\n")
            for line in lines[1:]:
                fields = line.split(",")
                if len(fields) == 2:
                    print(fields)
                    code = fields[0]
                    name = fields[1]
                    if code not in db_codes:
                        Product_Category(code=code, name=name).save()
            messages.success(request, 'Form submission successful')
    return render(request, "upload_csv.html")


def upload_product_csv(request):
    db_codes = {}
    p_list = Product.objects.all().values_list('code')
    for i in range(0, len(p_list)):
        db_codes[p_list[i][0]] = p_list[i][0]

    if request.method == "POST":
        csv_file = request.FILES["csv_file"]

        if not csv_file.name.endswith('.csv'):
            messages.error(request, 'This is not a csv file')
        else:
            file_data = csv_file.read().decode("utf-8")
            lines = file_data.split("\n")
            for line in lines[1:]:
                fields = line.split(",")
                if len(fields) == 3:
                    code = fields[0]
                    name = fields[1]
                    category = fields[2]
                    category = Product_Category.objects.get(code=category)
                    # if category not in Product_Category.objects.all():
                    if fields[0] not in db_codes:
                        Product(code=code, name=name, category=category).save()
            messages.success(request, 'Form submission successful')
    return render(request, "upload_product_csv.html")
