from django.db import models
from django.urls import reverse
from django.utils import timezone

class Wishlist(models.Model):
    PRIORITY_CHOICES = [
        ('H', 'High'),
        ('M', 'Medium'),
        ('L', 'Low'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    priority = models.CharField(max_length=1, choices=PRIORITY_CHOICES, default='M')
    is_private = models.BooleanField(default=False)
    estimated_cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    target_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('wishlist-detail', kwargs={'pk': self.pk})

class WishlistItem(models.Model):
    STATUS_CHOICES = [
        ('W', 'Wanted'),
        ('P', 'Purchased'),
        ('R', 'Received'),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    url = models.URLField(max_length=200, blank=True)
    image = models.ImageField(upload_to='wishlist_items/', blank=True, null=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='W')
    wishlist = models.ForeignKey(Wishlist, on_delete=models.CASCADE, related_name='items')
    priority = models.IntegerField(default=1)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['priority']