from django.urls import path
import consumptions.views

urlpatterns = [
    path('', consumptions.views.index, name='index'),
    path('api/', consumptions.views.ConsumptionApi.as_view(), name='api'),
    path('api/create/', consumptions.views.ConsumptionCreateApi.as_view(), name='api_create'),
    path('api/<int:pk>/update/', consumptions.views.ConsumptionUpdateApi.as_view(), name='api_update'),
    path('api/<int:pk>/delete/', consumptions.views.ConsumptionDeleteApi.as_view(), name='api_delete'),
    path('consumptions/', consumptions.views.ConsumptionListView.as_view(), name='consumptions'),
    path('consumption/create/', consumptions.views.ConsumptionCreate.as_view(), name='consumption_create'),
    path('consumption/<int:pk>/update/', consumptions.views.ConsumptionUpdate.as_view(), name='consumption_update'),
    path('consumption/<int:pk>/delete/', consumptions.views.ConsumptionDelete.as_view(), name='consumption_delete'),
    path('upload/product-categories-csv/', consumptions.views.upload_product_categories_csv, name='upload_product_categories_csv'),
] 