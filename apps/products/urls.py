from django.conf.urls import patterns, include, url
from products.views import ProductList,ProductView, ProductCreate, ProductUpdate, delete_product
from django.contrib.auth.decorators import login_required, permission_required

urlpatterns = patterns('',
    #List view
    url(r'^$', login_required(ProductList.as_view()), name='product_list'),
    url('^(?P<pk>\d+)/$', ProductView.as_view(), name='product_details'),
    url('^create/$', ProductCreate.as_view(), name='product_create'),
    url(r'^(?P<pk>\d+)/update/$', ProductUpdate.as_view(), name='product_update'),
    url(r'^(?P<product_id>\d+)/delete$', delete_product,
        name='product_delete'),
)