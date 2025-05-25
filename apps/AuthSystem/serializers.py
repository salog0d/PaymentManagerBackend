from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import CustomUser


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    """
    Serializador personalizado para obtener tokens JWT
    """
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        
        # Agregar datos personalizados al token
        token['email'] = user.email
        token['username'] = user.username if user.username else user.email
        token['first_name'] = user.first_name
        token['last_name'] = user.last_name
        
        return token


class UserRegistrationSerializer(serializers.ModelSerializer):
    """
    Serializador para el registro de usuarios
    """
    password = serializers.CharField(
        write_only=True,
        validators=[validate_password]
    )
    

    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'first_name', 'last_name', 'password')

   

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user


class UserSerializer(serializers.ModelSerializer):
    """
    Serializador para mostrar información del usuario
    """
    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'username', 'first_name', 'last_name', 'date_joined', 'is_active')
        read_only_fields = ('id', 'date_joined')


class UserUpdateSerializer(serializers.ModelSerializer):
    """
    Serializador para actualizar información del usuario
    """
    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name')

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance


class ChangePasswordSerializer(serializers.Serializer):
    """
    Serializador para cambiar contraseña
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(
        required=True,
        validators=[validate_password]
    )
    new_password_confirm = serializers.CharField(required=True)

    def validate(self, attrs):
        if attrs['new_password'] != attrs['new_password_confirm']:
            raise serializers.ValidationError("Las nuevas contraseñas no coinciden.")
        return attrs

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError("La contraseña actual es incorrecta.")
        return value


class PasswordResetRequestSerializer(serializers.Serializer):
    """
    Serializador para solicitar reset de contraseña
    """
    email = serializers.EmailField(required=True)

    def validate_email(self, value):
        try:
            user = CustomUser.objects.get(email=value)
        except CustomUser.DoesNotExist:
            raise serializers.ValidationError("No existe un usuario con este email.")
        return value