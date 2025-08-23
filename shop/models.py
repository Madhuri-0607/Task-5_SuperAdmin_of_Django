from django.db import models

# Simple Product model for storing product details
class Product(models.Model):
    # Size options - stored as code (XS, S, etc.) with readable labels
    SIZE_CHOICES = [
        ('XS', 'Extra Small'),
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('XL', 'Extra Large'),
        ('XXL', 'Double Extra Large'),
    ]

    # Main product fields
    name = models.CharField(max_length=200)          # product name
    description = models.TextField()                 # description text
    price = models.DecimalField(max_digits=10, decimal_places=2)  # price with 2 decimals
    size = models.CharField(max_length=3, choices=SIZE_CHOICES)   # store size code

    def __str__(self):
        # return a readable string for admin panel etc.
        return f"{self.name} ({self.get_size_display()}) - ₹{self.price}"

    class Meta:
        # order products by price by default
        ordering = ['price']
