from django.urls import path

from . import views

urlpatterns = [
	#Leave as empty string for base url
	path('', views.store, name="store"),
    path('register/', views.registerPage, name="register"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('update/', views.update, name="update"),
    path('payment/', views.payment, name="payment"),
    path('login/', views.loginPage, name="login"),  
	path('logout/', views.logoutUser, name="logout"),
    path('home/',views.home,name='home'),
    path('store_main/', views.store_main, name="store_main"),
    path('detail/<id>/', views.detail, name="detail"),
    

 
 ]