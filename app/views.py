from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.contrib.auth.hashers import make_password, check_password
from rest_framework.decorators import api_view
from .models import *
from .serializers import *
import traceback

@api_view(['GET'])
def users(request):
    if request.method == 'GET':
        users = UserDetails.objects.all()
        serializer = UserDetailsSerializer(users, many=True)
        return Response(serializer.data)
    
@api_view(['POST', 'GET'])
def create_Employee(request):
    if request.method == 'POST':
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['password'] = make_password(serializer.validated_data['password'])
            user = Employee.objects.create(**serializer.validated_data)
            return Response({'message': 'User created successfully', 'user': serializer.data['username']}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def Customer_login(request):
    try:
            username = request.data.get('username')
            password = request.data.get('password')
            # Debugging: Print received username and password
            print("Received username:", username)
            print("Received password:", password)

            try:
                user = UserDetails.objects.get(name=username)
            except UserDetails.DoesNotExist:
                print("User not found")
                return JsonResponse({'login': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)

            if check_password(password, user.password):
                print("Password matched")
                return JsonResponse({'Message': 'login successfully', 'username': user.name,'membership':user.membership}, status=status.HTTP_200_OK)
            else:
                print("Password did not match")
                return JsonResponse({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
            # Print the full traceback to debug the issue
        traceback.print_exc()
        return JsonResponse({'error': 'Internal server error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def total_employees(request):
    users = Employee.objects.all()
    serializer = TotalEmployeeSerializer(users, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def create_user_details(request):
    name = request.data.get('name')
    membership = request.data.get('membership', 'silver') 
    password = request.data.get('password')
    subscribed = request.data.get('subscribed', False) 
    premium_amount= request.data.get('premium_amount') 

    if not name or not password:
        return JsonResponse({'error': 'Name and password are required'}, status=400)

    if UserDetails.objects.filter(name=name).exists():
        return JsonResponse({'error': 'Username already exists'}, status=400)

    # Set membership to gold if subscribed
    if subscribed and premium_amount ==20000:
        membership = 'gold'
    elif subscribed and premium_amount ==50000:
        membership = 'platinum'

    # Prepare data for serializer
    request.data['membership'] = membership  # Update membership in request data

    serializer = UserDetailsSerializer(data=request.data)
    if serializer.is_valid():
        # Hash the password before saving
        serializer.validated_data['password'] = make_password(serializer.validated_data['password'])
        user = UserDetails.objects.create(**serializer.validated_data)
        return Response({'message': 'User created successfully', 'user': serializer.data}, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def Emp_login(request):
    try:
        username = request.data.get('username')
        password = request.data.get('password')

        # Debugging: Print received username and password
        print("Received username:", username)
        print("Received password:", password)

        try:
            user = Employee.objects.get(username=username)
        except Employee.DoesNotExist:
            print("User not found")
            return JsonResponse({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)

        if check_password(password, user.password):
            print("Password matched")
            # Change success to True if password is matched
            return JsonResponse({
                'Message': 'Login successfully',
                'success': True,  # Set success to True
                'username': user.username,
                'role': user.role
            }, status=status.HTTP_200_OK)
        else:
            print("Password did not match")
            return JsonResponse({'error': 'Invalid credentials','success': False }, status=status.HTTP_400_BAD_REQUEST)

    except Exception as e:
        # Print the full traceback to debug the issue
        traceback.print_exc()
        return JsonResponse({'error': 'Internal server error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def get_saloon_orders(request):
    orders = SaloonOrder.objects.all()
    serializer = SaloonOrdersSerializer(orders, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


# @csrf_exempt
@api_view(['POST'])
def post_saloon_orders(request):
    if request.method == 'POST':
        serializer = SaloonOrdersSerializer(data=request.data)
        print(request.data)  # This prints the full request data for debugging
        
        if serializer.is_valid():
            serializer.save()  # Save the validated data
            print(serializer)

            return Response({'message': 'Order success', 'order': serializer.data}, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def post_gym_orders(request):
    if request.method == 'POST':
        serializer = GymOrderSerializer(data=request.data)
        print(request.data)  # This prints the full request data for debugging
        
        if serializer.is_valid():
            serializer.save()  # Save the validated data
            print(serializer)

            return Response({'message': 'Order success', 'order': serializer.data}, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET'])
def get_gym_orders(request):
    orders = GymOrder.objects.all()
    serializer = GymOrderSerializer(orders, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)