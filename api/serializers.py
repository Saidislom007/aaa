from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import authenticate
from .models import (
    Conference,
    WordPart,
    Shoba,
    Maqola,
    AboutShoba,
    User

)



class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'password', 'password2']
        extra_kwargs = {'email': {'required': True}}

    def validate_email(self, value):
        if User.objects.filter(email__iexact=value).exists():
            raise serializers.ValidationError("Bu email allaqachon ro'yxatdan o'tgan.")
        return value

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({'password2': 'Parollar bir xil emas.'})
        return attrs

    def create(self, validated_data):
        validated_data.pop('password2')
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user

    
    

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        user = authenticate(username=attrs['username'], password=attrs['password'])
        if not user:
            raise serializers.ValidationError("Username yoki parol noto'g'ri.")
        if not user.is_active:
            raise serializers.ValidationError('Akkaunt faol emas.')
        attrs['user'] = user
        return attrs


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id' , 'username' , 'email' , 'first_name' , 'last_name']


class DownloadConferenceWordFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = WordPart
        fields = ['word_fayl']





class WordPartSerializer(serializers.ModelSerializer):
    class Meta:
        model = WordPart
        fields = '__all__'


class AboutSerializer(serializers.ModelSerializer):  
    class Meta:
        model = AboutShoba
        fields = '__all__'


class MaqolaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maqola
        fields = '__all__'

class AboutmoqolaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conference
        fields = 'title'


class ShobaSerializer(serializers.ModelSerializer):
    maqolalar = MaqolaSerializer(many=True, read_only=True)
    about = AboutSerializer(many=True, read_only=True)

    class Meta:
        model = Shoba
        fields = '__all__'




class ConferenceSerializer(serializers.ModelSerializer):
    word_parts = WordPartSerializer(many=True, read_only=True)
    shobalar = ShobaSerializer(many=True, read_only=True)


    
    model = Conference
    fields = '__all__'