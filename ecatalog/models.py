from django.db import models

class User(models.Model):
      name = models.CharField(max_length=200, null=True)
      email = models.CharField(max_length=200, null=True)
      password = models.CharField(max_length=200, null=True)

      def __str__(self):
            return self.name

class Product(models.Model):
      name = models.CharField(max_length=200, null=True)
      price = models.DecimalFieldField(max_digits=10, decimal_places=2)
      #image = models.imageField(upload_to='', null=True)
      description = models.TextField()
      created_at = models.DateTimeField(auto_now_add=True)
      updated_at = models.DateTimeField(auto_now=True)

      def __str__(self):
            return self.name

class Order(models.Model):
      user = models.ForeignKey(User, on_delete=models.SET_NULL,blank=True,null=True)
      created_at = models.DateTimeField(auto_now_add=True)
      updated_at = models.DateTimeField(auto_now=True)

      def __str__(self):
            return str(self.id)


class OrederLineItem(models.Model):
      product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
      order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
      quantity = models.IntegerField(default=0,null=True,blank=True)
      price = models.FloatField(max_length=200, null=True)
      created_at = models.DateTimeField(auto_now_add=True)
      updated_at = models.DateTimeField(auto_now=True)

      def __str__(self):
            return self.name

class Cart(model.Model):
      user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
      product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
      created_at = models.DateTimeField(auto_now_add=True)
      updated_at = models.DateTimeField(auto_now=True)

      def __str__(self):
            return str(self.id)












