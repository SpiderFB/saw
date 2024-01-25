from django.db import models
import uuid

class category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class productdb(models.Model):
    product_uuid = models.UUIDField(default=uuid.uuid4, unique=True, editable=False, primary_key=1)
    product_name = models.CharField(max_length=20)
    product_description = models.TextField()
    product_category = models.ForeignKey('category', on_delete=models.CASCADE)
    product_price = models.IntegerField()
    product_quantity = models.IntegerField()
    product_image = models.ImageField(upload_to='product')
    product_brand = models.CharField(default= 'Generic', max_length = 10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.product_uuid, self.product_name}"