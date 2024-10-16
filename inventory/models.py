from django.db import models
from django.utils import timezone

class Monument(models.Model):
    name = models.CharField(max_length=200)  # Person handling the monument
    from_person = models.CharField(max_length=200)  # Previous handler
    monument = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    weight = models.DecimalField(max_digits=6, decimal_places=2)
    length = models.DecimalField(max_digits=6, decimal_places=2)
    width = models.DecimalField(max_digits=6, decimal_places=2)
    height = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.PositiveIntegerField()
    status = models.CharField(max_length=50)  # Current stage (Owner, Polisher, Designer, Stock)

    owner_created_at = models.DateTimeField(null=True, blank=True)
    owner_updated_at = models.DateTimeField(null=True, blank=True)
    polisher_created_at = models.DateTimeField(null=True, blank=True)
    polisher_updated_at = models.DateTimeField(null=True, blank=True)
    designer_created_at = models.DateTimeField(null=True, blank=True)
    designer_updated_at = models.DateTimeField(null=True, blank=True)
    stock_created_at = models.DateTimeField(null=True, blank=True)
    stock_updated_at = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return f'{self.monument} handled by {self.name}'

class ProcessFlow(models.Model):
    monument = models.ForeignKey(Monument, on_delete=models.CASCADE)
    from_stage = models.CharField(max_length=50)
    to_stage = models.CharField(max_length=50)
    transferred_quantity = models.PositiveIntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.transferred_quantity} from {self.from_stage} to {self.to_stage} for {self.monument}'
