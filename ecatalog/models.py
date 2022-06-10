from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Product(TimeStampMixin):
      name = models.CharField(max_length=200, null=True)
      price = models.DecimalField(max_digits=10, decimal_places=2)
      #image = models.ImageField(upload_to='', null=True)
      description = models.TextField()

      def __str__(self):
            return self.name

      def get_absolute_url(self):
            """Returns the URL to access a detail record for this product."""
            return reverse('product-detail', args=[str(self.id)])


class Order(TimeStampMixin):
      user = models.ForeignKey(User, on_delete=models.CASCADE)

      def __str__(self):
            return str(self.id)


class OrederLineItem(TimeStampMixin):
      product = models.ForeignKey(Product, on_delete=models.CASCADE)
      order = models.ForeignKey(Order, on_delete=models.CASCADE)
      quantity = models.IntegerField(default=1,null=True,blank=True)
      price = models.FloatField(max_length=200, null=True)

      def __str__(self):
            return self.name


class Cart(TimeStampMixin):
      user = models.ForeignKey(User, on_delete=models.CASCADE)
      product = models.ForeignKey(Product, on_delete=models.CASCADE)
      quantity = models.IntegerField(default=1, null=True, blank=True)

      def __str__(self):
            return str(self.id)