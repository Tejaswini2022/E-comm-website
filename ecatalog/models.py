from django.db import models
from django.contrib.auth.models import User


class BaseClass(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Product(BaseClass):
      name = models.CharField(max_length=200, null=True)
      price = models.DecimalField(max_digits=10, decimal_places=2)
      #image = models.imageField(upload_to='', null=True)
      description = models.TextField()

      def __str__(self):
            return self.name

class Order(BaseClass):
      user = models.ForeignKey(User, on_delete=models.CASCADE)

      def __str__(self):
            return str(self.id)


class OrederLineItem(BaseClass):
      product = models.ForeignKey(Product, on_delete=models.CASCADE)
      order = models.ForeignKey(Order, on_delete=models.CASCADE)
      quantity = models.IntegerField(default=1,null=True,blank=True)
      price = models.FloatField(max_length=200, null=True)

      def __str__(self):
            return self.name

class Cart(BaseClass):
      user = models.ForeignKey(User, on_delete=models.CASCADE)
      product = models.ForeignKey(Product, on_delete=models.CASCADE)
      quantity = models.IntegerField(default=1, null=True, blank=True)

      def __str__(self):
            return str(self.id)












