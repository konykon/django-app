from django.urls import include, path
from rest_framework import routers
import consumptions.views


router = routers.DefaultRouter()
router.register('consumptions-api', consumptions.views.ConsumptionViewSet)

app_name = 'consumptions'

urlpatterns = [
    path('', include(router.urls)),
    path('home/', consumptions.views.Index.as_view(), name='index'),
    path('consumption-list/', consumptions.views.ConsumptionList.as_view(), name='consumption_list'),
    path('consumption/create/', consumptions.views.ConsumptionCreate.as_view(), name='consumption_create'),
    path('consumption/<int:pk>/update/', consumptions.views.ConsumptionUpdate.as_view(), name='consumption_update'),
    path('consumption/<int:pk>/delete/', consumptions.views.ConsumptionDelete.as_view(), name='consumption_delete'),
    path('upload/product-categories-csv/', consumptions.views.upload_csv, name='upload_csv'),
    path('upload/product-csv/', consumptions.views.upload_product_csv, name='upload_product_csv'),
]
