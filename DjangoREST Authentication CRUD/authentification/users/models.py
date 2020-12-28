from datetime import datetime

import jwt

from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin

from rest_framework import serializers


class UserManager(BaseUserManager):


    def _create_user(self, username, password=None, **extra_fields):
        """
        Creates new User.
        Username and Password required.
        """

        if username is None:
            raise serializers.ValidationError('Users should have a username')
        if password is None:
            raise serializers.ValidationError('Users should have password')

        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user


    def create_user(self, username=None, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_active', True)

        if extra_fields['is_superuser'] == True:
            return self.create_superuser(username, password, **extra_fields)

        return self._create_user(username, password, **extra_fields)


    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise serializers.ValidationError('Superuser must have is_staff=True.')

        if extra_fields.get('is_superuser') is not True:
            raise serializers.ValidationError('Superuser must have is_superuser=True.')

        return self._create_user(username, password, **extra_fields)


class CustomUser(AbstractUser, PermissionsMixin):


    id = models.AutoField(primary_key=True, verbose_name='ID')
    username = models.CharField(max_length=150, unique='True', null=False, blank=False, verbose_name='Username')
    password = models.CharField(max_length=128, null=False, blank=False, verbose_name='Password')
    first_name = models.CharField(max_length=30, verbose_name='First name')
    last_name = models.CharField(max_length=150, verbose_name='Last name')
    is_active = models.BooleanField(default=False, verbose_name='Active')
    last_login = models.DateTimeField(auto_now=True, verbose_name='Last login')
    is_superuser = models.BooleanField(default=False, verbose_name='Superuser status')

    groups = None
    user_permissions = None

    objects = UserManager()


    def __str__(self):
        return self.username


    @property
    def token(self):
        return self._generate_jwt_token()


    def _generate_jwt_token(self):
        dt = datetime.now()
        token = jwt.encode(
                {
                    'id': self.pk,
                    'iat': int(dt.strftime('%S')),
                },
                settings.SECRET_KEY, algorithm='HS256'
            )

        return token.decode('utf-8')
