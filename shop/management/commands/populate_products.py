from django.core.management.base import BaseCommand
from shop.models import Product
from decimal import Decimal
import random

class Command(BaseCommand):
    help = 'Populates the database with sample products'
    
    def handle(self, *args, **options):
        # Clear existing products
        Product.objects.all().delete()
        
        # Create 30 sample products
        for i in range(1, 31):
            Product.objects.create(
                name=f"Product {i}",
                #description=f"This is product number {i} with great features",
                price=Decimal(random.uniform(299, 4999)).quantize(Decimal('0.00')),
                size=random.choice(['XS', 'S', 'M', 'L', 'XL', 'XXL'])
            )
        
        self.stdout.write(
            self.style.SUCCESS('Successfully created 30 products!')
        )