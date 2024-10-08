from django.contrib import admin
from.models import *

@admin.register(Employee)
class CustomEmployeeAdmin(admin.ModelAdmin):
    list_display= ['username','role','mobile','location','password','attendance','total_attendance','image','is_active']

@admin.register(UserDetails)
class UserDetailsAdmin(admin.ModelAdmin):
    list_display= ['name','password','membership','subscribed','premium_amount']


@admin.register(SaloonOrder)
class SaloonOrdersAdmin(admin.ModelAdmin):
    list_display= ['id','order_type','category','services','date','time','created_at']


@admin.register(GymOrder)
class GymOrderAdmin(admin.ModelAdmin):
    list_display= ['id','gender','category','price','created_at']