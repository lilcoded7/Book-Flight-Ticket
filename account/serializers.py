from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User


class RegisterUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields = ['username','email', 'password']

    def create(self, validated_data):
        password = validated_data.get("password")
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user


class LoginUserSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

    def validate(self, data):
        user = authenticate(username=data['username'], password=data['password'])
        if user and user.is_active:
            refresh = RefreshToken.for_user(user)
            data['access_token'] = str(refresh.access_token)
            data['refresh_token'] = str(refresh)
            # print('=============================')
            # print(data['access_token'])
            # print('=============================')
            return data
        raise serializers.ValidationError("Incorrect credentials")

