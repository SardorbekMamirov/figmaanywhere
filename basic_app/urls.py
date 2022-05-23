from django.urls import path,include
from .import views

app_name='basic_app'

urlpatterns = [
    path('',views.ListApi.as_view()),
    path('category/',views.CategoriesList.as_view()),
    path('category/<int:pk>/',views.DetailCategory.as_view()),
    path('product/',views.ProductList.as_view()),
    path('product/<int:pk>/',views.DetailProduct.as_view()),
    path('user/', views.ListCustomUser.as_view()),
    path('user/<int:pk>/', views.DetailCustomUser.as_view()),
    
    path('site/', views.SiteList.as_view()),
    path('site/<int:pk>/', views.SiteDetail.as_view()),
    
    path('zakaz/', views.ZakazList.as_view()),
    path('zakaz/<int:pk>/', views.ZakazDetail.as_view()),
]
