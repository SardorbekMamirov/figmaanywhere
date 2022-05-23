from django.shortcuts import render
from rest_framework import generics
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.views.generic import TemplateView
from . import models, serializers
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


# Create your views here.
class ListApi(generics.ListCreateAPIView):
    serializer_class = serializers.TokenSerializer
    queryset = models.TokenModel.objects.all()
    # authentication_classes = []
    # permission_classes = []


class CategoriesList(generics.ListCreateAPIView):
    serializer_class = serializers.CategorySerializer
    queryset = models.Categories.objects.all()
    # authentication_classes = []
    # permission_classes = []


class DetailCategory(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.CategorySerializer
    queryset = models.Categories.objects.all()


class ProductList(generics.ListCreateAPIView):
    serializer_class = serializers.ProductsSerializer
    queryset = models.Products.objects.all()


class DetailProduct(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.ProductsSerializer
    queryset = models.Products.objects.all()


class ListCustomUser(generics.ListCreateAPIView):
    queryset = models.MyUser.objects.all()
    serializer_class = serializers.UserSerializer


class DetailCustomUser(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.MyUser.objects.all()
    serializer_class = serializers.UserSerializer
    
    

class SiteList(generics.ListCreateAPIView):
    queryset = models.Site.objects.all()
    serializer_class = serializers.SiteSerializer


class SiteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Site.objects.all()
    serializer_class = serializers.SiteSerializer
    
    
class ZakazList(generics.ListCreateAPIView):
    queryset = models.Zakaz.objects.all()
    serializer_class = serializers.ZakazSerializer


class ZakazDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Site.objects.all()
    serializer_class = serializers.SiteSerializer    