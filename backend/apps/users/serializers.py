from .models import Users
from rest_framework import serializers
from django.contrib.auth.hashers import make_password,check_password
from secrets import token_hex
import datetime


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('id','name','email','token','token_expires')


class UserSignUpSerializer(serializers.ModelSerializer):
    email = serializers.CharField(required=True)
    password= serializers.CharField(required = True,write_only=True)
    token = serializers.CharField( read_only = True)
    token_expires = serializers.DateTimeField(read_only = True)

    class Meta:
        model = Users
        fields = ('id','name','email','password','token','token_expires')

    def create(self,validate_data):

        if Users.objects.filter(email = validate_data['email']).exists():
            raise serializers.ValidationError({'email':['This email already exists']})
        
        validate_data['password'] = make_password(validate_data['password'])
        validate_data['token'] =  token_hex(30)
        validate_data['token_expires'] = datetime.datetime.now() + datetime.timedelta(days=7)
        
        return super().create(validate_data)
    

class UserSignInSerializer(serializers.ModelSerializer):
    email = serializers.CharField(required=True)
    password= serializers.CharField(required = True,write_only=True)
    name = serializers.CharField(read_only=True)
    token = serializers.CharField( read_only = True)
    token_expires = serializers.DateTimeField(read_only = True)

    class Meta:
        model = Users
        fields = ('id','name','email','password','token','token_expires')

    def create(self, validated_data):

        user = Users.objects.filter(email =  validated_data['email'])
        if len(user) > 0 and check_password(validated_data['password'],user[0].password):
            user[0].token = token_hex(30)
            user[0].token_expires = datetime.datetime.now() + datetime.timedelta(days=7)
            user[0].save()

            return user[0]
        
        else:
            raise serializers.ValidationError({'error':'The email or password is incorrect.'})