
from django.db import models
from django.contrib.auth.models import BaseUserManager,PermissionsMixin,AbstractBaseUser
# Create your models here.
from django.utils import timezone


class TokenModel(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField()
    phone=models.CharField(max_length=15)
    img=models.ImageField(upload_to='images/')
    def __str__(self):
        return self.name

class Categories(models.Model):
    name=models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Products(models.Model):
    category=models.ForeignKey(Categories, on_delete=models.CASCADE)
    image=models.ImageField(upload_to='images/')
    price=models.CharField(max_length=200)
    quantity=models.PositiveIntegerField()
    ramka=models.CharField(max_length=200)
    razmer=models.IntegerField()
    depth=models.IntegerField()

    def __str__(self):
        return self.price

class MyManager(BaseUserManager):
    def create_user(self, username, **extra):
        if not username:
            raise ValueError('Username kiritilishi majburiy !')
        
        user=self.model(username=username, **extra)
        user.set_password(extra.get('password'))
        user.save()
        return user
    
    def create_superuser(self, username, **extra):
        extra.setdefault('is_staff', True)
        extra.setdefault('is_active', True)
        extra.setdefault('is_superuser', True)
        
        
        if not extra.get('is_staff'):
            raise ValueError("Superuser uchun is_staff True bo'lishi kerak")
        if not extra.get('is_active'):
            raise ValueError("Superuser uchun is_active True bo'lishi kerak")
        if not extra.get('is_superuser'):
            raise ValueError("Superuser uchun is_superuser True bo'lishi kerak")
        
        return self.create_user(username=username, **extra)
        
         
    
    
class MyUser(AbstractBaseUser, PermissionsMixin):
    username=models.CharField(max_length=30, unique=True)
    phone=models.CharField(max_length=30, unique=True, default=None, null=True, blank=True)
    email=models.EmailField(unique=True)
    
    date_joined=models.DateTimeField(auto_now_add=True)
    
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=True)
    is_superuser=models.BooleanField(default=True)
    
    USERNAME_FIELD='username'
    REQUIRED_FIELD=[]
    
    objects=MyManager()
    
    def __str__(self):
        return self.username

class Site(models.Model):
    tel=models.CharField(max_length=30, verbose_name='Телефонный номер')
    adres=models.CharField(max_length=150, verbose_name='Адрес')
    time=models.CharField(max_length=100, verbose_name='Рабочее времяxx')
    telegram=models.CharField(max_length=100, verbose_name='Телеграм')
    instagram=models.CharField(max_length=100, verbose_name='Инстаграм')
    
    def __str__(self) -> str:
        return self.tel


class Zakaz(models.Model):
    name=models.CharField(max_length=60, verbose_name='Ваше имя')
    phone=models.CharField(max_length=40, verbose_name='Ваше номер')
    
    def __str__(self):
        return self.name
    
