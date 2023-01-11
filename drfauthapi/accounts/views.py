from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializer import CustomerRegistartionSerializer,CustomerLoginSerializer,CustomerProfileSerializer,CustomerPasswordChangeSerializer
from django.contrib.auth import authenticate,login,logout
from accounts.renderers import CustomerRender
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


# Create your views here.
class CustomerRegistrationView(APIView):
    renderer_classes = [CustomerRender]
    def post(self, request,format=None):
        serializer = CustomerRegistartionSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            token = get_tokens_for_user(user)

            return Response({'token':token,'msg':'Registration Successful'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class CustomerLoginView(APIView):
    def post(self, request, format = None):
        serializer = CustomerLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.data.get('email')
            password = serializer.data.get('password')
            cust = authenticate(email=email,password=password)
            if cust is not None:
                token = get_tokens_for_user(cust)
                return Response({'token':token,'msg':'Login succsessfully'},status=status.HTTP_200_OK)
            else:
                return Response({'errors':{'non_fields_errors':['Email or Password is Not Valid']}},status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class CustomerProfileView(APIView):
    renderer_classes = [CustomerRender]
    permission_classes = [IsAuthenticated]
    def get(self,request,format=None):
        serializer = CustomerProfileSerializer(request.user)
        return Response(serializer.data,status=status.HTTP_200_OK)

class CustomerChangePasswordView(APIView):
    renderer_classes = [CustomerRender]
    permission_classes = [IsAuthenticated]
    def post(self, request,format=None):
        serializer = CustomerPasswordChangeSerializer(data=request.data,context={'user':request.user})
        if serializer.is_valid(raise_exception=True):
            return Response({'msg':"Password Change Successfully"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)