from rest_framework import serializers

from django.contrib.auth import authenticate

from ..models import CustomUser


class RegistrationSerializer(serializers.ModelSerializer):

    """
    Serializes 'POST' requests only.
    Creates a new user.
    Username, and password are required.
    Returns a Response with users data.
    """

    password = serializers.CharField(
            max_length=128,
            min_length=8,
            write_only=True,
        )


    class Meta:
        model = CustomUser
        fields = [
                'id',
                'username',
                'first_name',
                'last_name',
                'password',
                'is_active',
                'is_superuser',
                'last_login',
                'token'
            ]


    token = serializers.CharField(max_length=255, read_only=True)


    def create(self, data):
        return CustomUser.objects.create_user(**data)


class LoginSerializer(serializers.Serializer):

    """
    Authenticates an existing user.
    Username and password are required.
    Returns a JSON web token.
    """

    username = serializers.CharField(max_length=255, write_only=True)
    password = serializers.CharField(max_length=128, write_only=True)

    # Ignore these fields if they are included in the request.
    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):
        """
        Validates user data.
        """

        username = data.get('username', None)
        password = data.get('password', None)

        if username is None:
            raise serializers.ValidationError(
                'A username is required to log in.'
            )

        if password is None:
            raise serializers.ValidationError(
                'A password is required to log in.'
            )

        user = authenticate(username=username, password=password)

        if user is None:
            raise serializers.ValidationError(
                'A user with this username and password was not found.'
            )

        if not user.is_active:
            raise serializers.ValidationError(
                'This user has been deactivated.'
            )

        return {
                'token': user.token,
            }


class ReadOnlyUserSerializer(serializers.ModelSerializer):

    """
    Serializes 'GET' requests only.
    """

    class Meta:
        model = CustomUser
        fields = [
                'id',
                'username',
                'is_active',
                'first_name',
                'last_name',
                'is_active',
                'last_login',
                'is_superuser',
            ]
        read_only = [
                'id',
                'last_login',
                'is_superuser',
            ]


class WriteOnlyUserSerializer(serializers.ModelSerializer):

    """
    Serializes 'PUT', 'PATCH' requests only.
    """

    class Meta:
        model = CustomUser
        fields = [
                'id',
                'username',
                'is_active',
                'first_name',
                'last_name',
                'last_login',
                'is_superuser',
            ]

        read_only = [
                'id',
                'last_login',
                'is_superuser',
            ]
