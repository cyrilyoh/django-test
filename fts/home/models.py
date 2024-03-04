from django.db import models

class Colour(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Colour name')
    paint_code = models.CharField(max_length=50, unique=True, verbose_name='Paint code')
    
    def __str__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Brand name')
    
    def __str__(self):
        return self.name

class Car(models.Model):
    CONDITION_CHOICES = (
        ('New', 'New'),
        ('Used', 'Used')
    )
    
    model = models.CharField(max_length=100, verbose_name='Model')
    colour = models.ForeignKey(Colour, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    condition = models.CharField(max_length=20, choices=CONDITION_CHOICES, verbose_name='Condition')
    no_previous_owners = models.IntegerField(default=0, verbose_name='No. of previous owners')
    
    def __str__(self):
        return f"{self.brand} {self.model}"

class OwnerRecord(models.Model):
    owner = models.CharField(max_length=100, verbose_name='Owner name')
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    owned_from = models.DateField(verbose_name='Owned from')
    owned_to = models.DateField(null=True, blank=True, verbose_name='Owned to',)
    
    def __str__(self):
        return f"{self.name} - {self.car}"
