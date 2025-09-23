import uuid
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User



# class Employee(models.Model):
#   user_name = models.CharField(max_length=255)
#   user_age = models.IntegerField()
#   user_persona = models.TextField() # satu teks, satu varchar, perbedaannya: varchar digunakan utk teks yg udh pasti panjangnya (ada max line, terkhusus yg pendek). teksfield digunakan untuk teks yg panjang (desk produk, blog)


class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    CATEGORY_CHOICES = [
        ('men', 'Men'),
        ('women', 'Women'),
        ('kids', 'Kids'),
        ('accessories', 'Accessories'),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    price = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True)
    thumbnail = models.URLField(blank=True)   
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='men')
    is_featured = models.BooleanField(default=False)
    stock = models.IntegerField(default=0)
    brand = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    product_views = models.PositiveIntegerField(default=0)

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

    def increment_views(self):
        self.product_views = (self.product_views or 0) + 1
        self.save()

    


# model baru, employee (name (maks 255),nama,age,persona (teks panjang tdk ada batas karakter)
