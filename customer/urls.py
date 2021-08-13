from django.urls import path
from . import views

urlpatterns = [
	path('registercustomer', views.registercustomer, name='registercustomer'),
	path('logincustomer', views.logincustomer, name='logincustomer'),
	path('logout', views.logoutcustomer, name='logoutcustomer'),
	path('products', views.homepage, name='products'),
	path('addtocart', views.addproducttocart, name='addtocart'),
    path('removefromcart', views.removeproductfromcart, name='removefromcart'),
    path('viewcustomercart', views.viewcustomercart, name='viewcustomercart'),
    path('removefromcartpage/<int:cart_item_id>', views.removeproductcartpage, name='removeproductcartpage'),
]