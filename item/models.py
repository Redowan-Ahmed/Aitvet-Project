from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=255)
    image=models.ImageField(upload_to='category_images', blank=True, null=True)


    class Meta:
        ordering = ('name',)
        verbose_name_plural='Categories'

    def __str__(self) -> str:
        return self.name
    
class Item(models.Model):
    category=models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    name=models.CharField(max_length=255, null=True)
    description=models.TextField()
    price=models.FloatField()
    image=models.ImageField(upload_to='items_images', blank=True, null=True)
    is_sold=models.BooleanField(default=False)
    contact_number = models.CharField(max_length=15, default='01632398271')
    created_by=models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)
        verbose_name_plural='items'

    def __str__(self) -> str:
        return self.name