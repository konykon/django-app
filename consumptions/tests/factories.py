import factory
from datetime import datetime
from consumptions.models import Consumption, Product_Category, Product


class Product_Category_Factory(factory.Factory):
    class Meta:
        model = Product_Category

    code = 'LL'
    name = 'Landline'


class Product_Factory(factory.Factory):
    class Meta:
        model = Product

    code = 'LL001'
    name = 'ADSL'
    category = factory.SubFactory(Product_Category_Factory)


class Consumption_Factory(factory.Factory):
    class Meta:
        model = Consumption

    id = factory.Sequence(lambda n: n)
    timestamp = factory.LazyFunction(datetime.now)
    product = factory.SubFactory(Product_Factory)
    quantity = 10
