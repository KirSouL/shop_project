from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ProductDetailView, ProductDeleteView, ProductCreateView, ProductUpdateView, \
    contacts, category

app_name = CatalogConfig.name

urlpatterns = [
    path('create_product/', ProductCreateView.as_view(), name='create_product'),
    path('', ProductListView.as_view(), name='product_list'),
    path('contacts/', contacts, name='contacts'),
    path('category/', category, name='category'),
    path('product_detail/<int:pk>', ProductDetailView.as_view(), name='product_detail'),
    path('delete/<int:pk>', ProductDeleteView.as_view(), name='delete'),
    path('update_product/', ProductCreateView.as_view(), name='update_product'),

]
