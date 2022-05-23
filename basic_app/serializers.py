from rest_framework import serializers

from . import models


class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TokenModel
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Categories
        fields = '__all__'


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Products
        fields = '__all__'




class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MyUser
        fields = '__all__'

    # def create(self, validated_data):
    #     return models.MyUser.objects.create_user(**validated_data)

class SiteSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Site
        fields='__all__'

class ZakazSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Zakaz
        fields='__all__'
