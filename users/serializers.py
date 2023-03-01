from rest_framework import serializers
from rest_framework.validators import ValidationError
from rest_framework.authtoken.models import Token
from .models import User


class SignupSerializer(serializers.ModelSerializer):
    email = serializers.CharField(max_length=50)
    username = serializers.CharField(max_length=50)
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        # validations

        model = User
        fields = ['email', 'username', 'password']

#  Check is emmail exist in database

    def validate(self, attrs):
        email_exist = User.objects.filter(email=attrs['email']).exists()

        if email_exist:
            raise ValidationError("email has already been used")
        return super().validate(attrs)

    # create a function to hash the password using the validated data

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = super().create(validated_data)
        user.set_password(password)
        user.save() #this saves to the database

        # create a token that belongs to the specific user created 
        Token.objects.create(user=user)
        return user
