from rest_framework import serializers
from accounts.models import Customer


class CustomerRegistartionSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type':'password'},write_only=True)
    class Meta:
        model = Customer
        fields = ['name','email','password','password2','tc']
        extra_kwargs={
            'password':{'write_only':True}
        }
    
    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')
        if password != password2:
            raise serializers.ValidationError("Password did't Match ")
        return attrs
    
    def create(self, validated_data):
        return Customer.objects.create_user(**validated_data)

class CustomerLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)
    class Meta:
        model = Customer
        fields = ['email','password']