from django.db import models


class Shopping(models.Model):
    Type = [("CHILD", "child"),("MEN", "men"), ("WOMEN", "women"), ("HOME", "home"), ("KITCHEN", "kitchen")]
    Payment = [("ONLINE", "online"), ("CASH ON DELIVERY", "cash on delivery")]
    category = models.CharField(max_length=10,  choices=Type)
    product_name = models.CharField(max_length=20)
    product_price = models.FloatField()
    product_quantity = models.IntegerField()
    payment_method = models.CharField(max_length=20, choices=Payment)
    created_on = models.DateField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)


