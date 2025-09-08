import uuid
from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('men', 'Men'),
        ('women', 'Women'),
        ('kids', 'Kids'),
        ('accessories', 'Accessories'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    is_featured = models.BooleanField(default=False)
    stock = models.IntegerField(default=0)
    brand = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.category})"

    @property
    def is_in_stock(self):
        return self.stock > 0

    def sell(self, quantity=1):
        if self.stock >= quantity:
            self.stock -= quantity
            self.save()
            return True
        return False
