from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ProductDetailView, ProductDeleteView, ProductCreateView, ProductUpdateView, \
    category, BlogListView, BlogCreateView, BlogUpdateView, BlogDetailView, BlogDeleteView, ContactsView

app_name = CatalogConfig.name

urlpatterns = [
    path('create_product/', ProductCreateView.as_view(), name='create_product'),
    path('', ProductListView.as_view(), name='product_list'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('category/', category, name='category'),
    path('product_detail/<int:pk>', cache_page(60)(ProductDetailView.as_view()), name='product_detail'),
    path('delete/<int:pk>', cache_page(60)(ProductDeleteView.as_view()), name='delete'),
    path('update_product/<int:pk>', cache_page(60)(ProductUpdateView.as_view()), name='update_product'),
    path('blog/', BlogListView.as_view(), name='blog_list'),
    path('create_blog/', BlogCreateView.as_view(), name='create_blog'),
    path('edit_blog/<int:pk>', BlogUpdateView.as_view(), name='edit'),
    path('view_blog/<int:pk>', BlogDetailView.as_view(), name='view'),
    path('delete_blog/<int:pk>', BlogDeleteView.as_view(), name='delete_blog')

]
