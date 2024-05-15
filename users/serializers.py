from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from rest_framework.validators import UniqueValidator
from users.models import CustomUser
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        token['email'] = user.email
        # ...

        return token


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    email = serializers.EmailField(required=True,
                                   validators=[UniqueValidator(queryset=CustomUser.objects.all())]
                                   )
    phone = serializers.CharField(required=True,
                                  validators=[UniqueValidator(queryset=CustomUser.objects.all())]
                                  )
    full_name = serializers.CharField(max_length=100, required=True)

    class Meta:
        model = CustomUser
        fields = ('id', 'phone', 'full_name', 'email', 'password', 'password2')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = CustomUser.objects.create(
            phone=validated_data['phone'],
            full_name=validated_data['full_name'],
            email=validated_data['email']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user


# from django.contrib.auth.password_validation import validate_password
# from rest_framework import serializers
# from rest_framework.validators import UniqueValidator
# from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
#
# from users.models import CustomUser
#
#
# class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
#     @classmethod
#     def get_token(cls, user):
#         token = super().get_token(user)
#
#         # Add custom claims
#         token['username'] = user.username
#         token['email'] = user.email
#         # ...
#
#         return token
#
#
# class RegisterSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(
#         write_only=True, required=True, validators=[validate_password])
#     password2 = serializers.CharField(write_only=True, required=True)
#     email = serializers.EmailField(required=True,
#                                    validators=[UniqueValidator(queryset=CustomUser.objects.all())]
#                                    )
#
#     class Meta:
#         model = CustomUser
#         fields = ('username', 'email', 'password', 'password2')
#
#     def validate(self, attrs):
#         if attrs['password'] != attrs['password2']:
#             raise serializers.ValidationError({"password": "Password fields didn't match."})
#
#         return attrs
#
#     def create(self, validated_data):
#         user = CustomUser.objects.create(
#             # username=validated_data['username'],
#             email=validated_data['email']
#         )
#
#         user.set_password(validated_data['password'])
#         user.save()
#
#         return user
#
#
# class ProfileSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CustomUser
#         fields = '__all__'