from django.db import models

class License(models.Model):
    STATUS_CHOICES = (
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    )
    
    LICENSE_TYPE_CHOICES = (
        ('perpetual', 'Perpetual'),
        ('subscription', 'Subscription'),
        ('Temporary', 'Temporary'),
    )
    
    category = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField( null=True, blank=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    unit = models.CharField(max_length=20)
    location = models.CharField(max_length=250, null=True, blank=True)
    tag = models.CharField(max_length=20, null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')
    terms = models.TextField()
    license_type = models.CharField(max_length=20, choices=LICENSE_TYPE_CHOICES)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title