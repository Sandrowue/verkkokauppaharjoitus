from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    tax = models.DecimalField(max_digits=7, decimal_places=0)

    def __str__(self):
        return self.name
    
    @property
    def total_price(self):
        return self.price * (1 + self.tax/100)
    

class Order(models.Model):
    order_name = models.CharField(max_length=100)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    email = models.EmailField()
    paid = models.BooleanField(default=False)

    def __str__(self):
        return self.order_name