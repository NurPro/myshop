from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm
from product.models import Product
# Create your models here.

class ShopCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField()

    def __str__(self):
        return self.product.title
    @property
    def price(self):
        return (self.product.price)

    @property
    def amount(self):
        return (self.quantity*self.product.price)

class ShopCartForm(ModelForm):
    class Meta:
        model = ShopCart
        fields = ['quantity']
class Order(models.Model):
    STATUS=(
        ('New', 'Yangi'),
        ('Accepted', 'Qabul qilingan'),
        ('Preparing', 'Tayyorlanish'),
        ('OnShipping', 'Yetkazib berishga'),
        ('Completed', 'Tugallangan'),
        ('Cancelled', 'Bekor qilingan'),
    )
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    phone_code = models.CharField(max_length=3, editable=False)
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    phone = models.CharField(max_length=15)
    address = models.CharField(blank=True, max_length=255)
    city = models.CharField(blank=True, max_length=55)
    country = models.CharField(blank=True, max_length=55)
    total = models.FloatField()
    status = models.CharField(max_length=15, choices=STATUS, default='New')
    ip = models.CharField(blank=True, max_length=25)
    adminnote = models.CharField(blank=True, max_length=100)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.first_name

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'address', 'phone', 'city', 'country']

class OrderProduct(models.Model):
    STATUS = (
        ('New', 'Yangi'),
        ('Accepted', 'Qabul qilingan'),
        ('Cancelled', 'Bekor qilingan'),
    )
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.FloatField()
    quantity = models.IntegerField()
    amount = models.FloatField()
    status = models.CharField(max_length=15, choices=STATUS, default='New')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.title
