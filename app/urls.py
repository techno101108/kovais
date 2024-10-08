from django.urls import path

from .views import *

# from .views import video_processing_view

urlpatterns = [
    path('users/',users),
    path('customer-login/',Customer_login),
    path('total-employees/', total_employees, name='total_users'),
    path('create-employee/', create_Employee, name='create_user'),
    path('Employee-login/', Emp_login),
    path('create-customer/',create_user_details),


    # saloon

    path('get/saloon/orders/',get_saloon_orders),
    path('saloon/orders/',post_saloon_orders),

    #gym
    path('get/gym/orders/',get_gym_orders),
    path('gym/orders/',post_gym_orders),

]