from django.db import models

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=50) 

class Product(models.Model):
    product_name = models.CharField(max_length=50)
    product_detail = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    category = models.ForeignKey('Category', related_name='product', on_delete=models.CASCADE)
    is_soldout = models.BooleanField(default=False)
    
class Order(models.Model):
    products = models.ManyToManyField('Product', through='Product_Order', related_name= 'ordered')
    payment = models.CharField(max_length=50)
    is_takeout = models.BooleanField(default=True)
    total_price = models.IntegerField()
    
class Product_Order(models.Model):
    product = models.ForeignKey('Product', related_name='order_detail', on_delete=models.SET_NULL, null = True)
    order = models.ForeignKey('Order', related_name='order_detail',on_delete=models.SET_NULL, null = True)
    order_num = models.IntegerField()
    price = models.IntegerField() #상품개수 * 단가
    
    