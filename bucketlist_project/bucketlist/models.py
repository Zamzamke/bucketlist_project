from django.contrib.auth.models import User
from django.db import models

#Bucketlist models
class BucketList(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    owner = models.ForeignKey(User, related_name='bucketlists', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


 #Models to categorize items
class BucketListItem(models.Model):
    CATEGORY_CHOICES = (
        ('travel', 'Travel'),
        ('career', 'Career'),
        ('personal', 'Personal'),
    )
    
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('completed', 'Completed'),
    )

    bucketlist = models.ForeignKey(BucketList, related_name="items", on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='personal')
    priority = models.IntegerField(default=0)  # You can set this to range from 1 (high) to 5 (low)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return self.title
 