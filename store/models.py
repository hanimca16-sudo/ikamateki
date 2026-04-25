from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    SHIPPING_CHOICES = [
        ('available',     'شحن متوفر'),
        ('local',         'شحن جزئي'),
        ('not_available', 'شحن غير متوفر'),
    ]
    RESIDENCE_CHOICES = [
        ('1',       'إقامة 1'),
        ('2',       'إقامة 2'),
        ('3',       'إقامة 3'),
        ('outside', 'خارج الإقامة'),
    ]
    seller      = models.ForeignKey(User, on_delete=models.CASCADE)
    title       = models.CharField(max_length=200)
    description = models.TextField()
    price       = models.DecimalField(max_digits=8, decimal_places=2)
    image       = models.ImageField(upload_to='products/', blank=True)
    stock       = models.IntegerField(default=0)
    shipping    = models.CharField(max_length=20, choices=SHIPPING_CHOICES, blank=True)
    wilaya      = models.CharField(max_length=100, blank=True)
    phone       = models.CharField(max_length=20, blank=True)
    residence   = models.CharField(max_length=10, choices=RESIDENCE_CHOICES, default='1')
    created_at  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title