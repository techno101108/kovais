from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Employee(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('member','Member'),
        ('saloon','Saloon'),
        ('spa','Spa'),
        ('gym','Gym'),
        ('hotel','Hotel')
    )
 
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='member')
    mobile=models.CharField(max_length=255,null=True,blank=True)
    location = models.CharField(max_length=255,blank=True,null=True)
    password = models.CharField(max_length=255)
    attendance= models.CharField(max_length=15,null=True,blank=True)
    total_attendance=models.CharField(max_length=255,blank=True,null=True)
    image=models.CharField(max_length=255,blank=True,null=True)
    is_active = models.BooleanField(default=True)
    success =models.BooleanField(default=False)
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        related_name='Employee',  # Unique related name for groups
        related_query_name='Employee',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        related_name='Employee',  # Unique related name for user permissions
        related_query_name='Employee',
    )  
  

    
class UserDetails(models.Model):
    MEMBERSHIP_CHOICES = (
        ('silver','Silver'),
        ('gold','Gold'),
        ('platinum','Platinum'),
    )
    name= models.CharField(max_length=256,blank=True,null=True)
    membership = models.CharField(max_length=20, choices=MEMBERSHIP_CHOICES, default='silver')
    password = models.CharField(max_length=255)
    subscribed=models.BooleanField(default=False)
    premium_amount =models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class Bonus(models.Model):
    name =models.ForeignKey(Employee,on_delete=models.CASCADE)
    points=models.CharField(max_length=256,null=True,blank=True)
    is_active = models.BooleanField(default=True)
    
class Booking(models.Model):
    customer_id=models.ForeignKey(UserDetails, on_delete=models.CASCADE)
    employee_id=models.ForeignKey(Employee, on_delete=models.CASCADE)
    time_slot=models.DateTimeField(auto_now=True)
    bonus=models.ForeignKey(Bonus,on_delete=models.CASCADE)

class SaloonOrder(models.Model):
    order_type = models.CharField(max_length=255,null=True,blank=True)
    category=models.CharField(max_length=255,null=True,blank=True)
    services=models.TextField(null=True,blank=True)
    date=models.DateField(null=True,blank=True)
    time=models.CharField(max_length=255,null=True,blank=True)
    created_at =models.DateTimeField(auto_now_add=True)

    

class GymOrder(models.Model):
    gender=models.CharField(max_length=255,null=True,blank=True)
    category=models.CharField(max_length=255,null=True,blank=True)
    price=models.TextField(null=True,blank=True)
    created_at =models.DateTimeField(auto_now_add=True)