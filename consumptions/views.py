from django.shortcuts import render
from consumptions.models import Product, Product_Category, Consumption
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.

def index(request):
    num_products = Product.objects.count()

    context = {
        'num_products': num_products,
    }

    return render(request, 'index.html', context=context)

def base(request):
    return render(request, 'base.html')

class ConsumptionListView(generic.ListView):
    model = Consumption
    paginate_by = 10
    context_object_name = 'consumption_list'
    # queryset = Consumption.objects.filter(product__icontains='L')
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