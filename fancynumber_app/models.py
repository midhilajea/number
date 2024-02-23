# models.py
from django.db import models

class FancyPhoneNumber(models.Model):
    number = models.CharField(max_length=20)
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=True)  # Example field definition with null=True
    # price_range = models.CharField(max_length=50)  # New field for price range

    def __str__(self):
        return self.number
