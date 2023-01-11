from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializer import CustomerRegistartionSerializer,CustomerLoginSerializer
from django.contrib.auth import authenticate,login,logout
from accounts.renderers import CustomerRender

# Create your views here.
class CustomerRegistrationView(APIView):
    renderer_classes = [CustomerRender]
    def post(self, request,format=None):
        serializer = CustomerRegistartionSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'msg':'Registration Successful'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class CustomerLoginView(APIView):
    def post(self, request, format = None):
        serializer = CustomerLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.data.get('email')
            password = serializer.data.get('password')
            cust = authenticate(email=email,password=password)
            if cust is not None:
                return Response({'msg':'Login succsessfully'},status=status.HTTP_200_OK)
            else:
                return Response({'errors':{'non_fields_errors':['Email or Password is Not Valid']}},status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)