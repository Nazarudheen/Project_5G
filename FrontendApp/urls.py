from django.urls import path
from FrontendApp import views

urlpatterns = [
    path('Homepage/',views.Homepage,name="Homepage"),
    path('All_ProductsPage/',views.All_ProductsPage,name="All_ProductsPage"),
    path('Filtered_Products/<cat_name>/',views.Filtered_Products,name="Filtered_Products"),
    path('Contact_page/',views.Contact_page,name="Contact_page"),
    path('ContactSave/',views.ContactSave,name="ContactSave"),
    path('Aboutus_page/',views.Aboutus_page,name="Aboutus_page"),
    path('ServicesPage/',views.ServicesPage,name="ServicesPage"),
    path('UserSignUp_Page/',views.UserSignUp_Page,name="UserSignUp_Page"),
    path('SignupPage/',views.SignupPage,name="SignupPage"),
    path('LoginUser/',views.LoginUser,name="LoginUser"),
    path('user_logout/',views.user_logout,name="user_logout"),
    path('SaveCart/',views.SaveCart,name="SaveCart"),
    path('Cart_page/',views.Cart_page,name="Cart_page"),
    path('CheckoutPage/',views.CheckoutPage,name="CheckoutPage"),
    path('SingleProduct_page/<int:proid>/',views.SingleProduct_page,name="SingleProduct_page"),
    path('deleteCartItem/<int:cartid>/',views.deleteCartItem,name="deleteCartItem"),
]