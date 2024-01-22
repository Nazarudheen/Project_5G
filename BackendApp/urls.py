from django.urls import path
from BackendApp import views

urlpatterns = [
    path('Indexpage/',views.Indexpage,name="Indexpage"),
    path('CategoryPage/',views.CategoryPage,name="CategoryPage"),
    path('SaveCategory/',views.SaveCategory,name="SaveCategory"),
    path('DisplayCategory/',views.DisplayCategory,name="DisplayCategory"),
    path('EditCategory/<int:cid>/',views.EditCategory,name="EditCategory"),
    path('UpdateCategory/<int:cid>/',views.UpdateCategory,name="UpdateCategory"),
    path('deleteCategory/<int:cid>/',views.deleteCategory,name="deleteCategory"),

    path('AddProduct/',views.AddProduct,name="AddProduct"),
    path('SaveProduct/',views.SaveProduct,name="SaveProduct"),
    path('DisplayProduct/',views.DisplayProduct,name="DisplayProduct"),
    path('EditProduct/<int:pid>/',views.EditProduct,name="EditProduct"),
    path('UpdateProduct/<int:pid>/',views.UpdateProduct,name="UpdateProduct"),
    path('DeleteProduct/<int:pid>/',views.DeleteProduct,name="DeleteProduct"),

    path('LoginPage/',views.LoginPage,name="LoginPage"),
    path('Admin_login/',views.Admin_login,name="Admin_login"),
    path('Admin_logout/',views.Admin_logout,name="Admin_logout"),

    path('ContactPage/', views.ContactPage, name="ContactPage"),
    path('DeleteContact/<int:ctid>', views.DeleteContact, name="DeleteContact"),

]