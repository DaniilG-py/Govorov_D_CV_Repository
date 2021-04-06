from django.db import models
from django.contrib.auth.models import (
                                        AbstractUser,
                                        BaseUserManager,
                                    )



class UserManager(BaseUserManager):

    def _create_user(self, username, password=None, **extra_fields):
        if username is None:
            raise TypeError('Users should have a username')
        if password is None:
            raise TypeError('Users should have password')

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
            raise TypeError('Superuser must have is_staff=True.')

        if extra_fields.get('is_superuser') is not True:
            raise TypeError('Superuser must have is_superuser=True.')

        return self._create_user(username, password, **extra_fields)


class CustomUser(AbstractUser):

    id = models.AutoField(primary_key=True, verbose_name='ID')
    username = models.CharField(max_length=100, unique=True, db_index=True, verbose_name='Никнейм')
    password = models.CharField(max_length=128, null=False, blank=False, verbose_name='Пароль')
    email = models.EmailField(max_length=255, unique=True, db_index=True, help_text='Почта для связи с Вами.')
    first_name = models.CharField(max_length=200, verbose_name='Ваше имя')
    last_name = models.CharField(max_length=200, verbose_name='Ваша фамилия', null=True, blank=True)
    phone = models.CharField(max_length=20, verbose_name='Телефонный номер', null=True, blank=True)
    company_name = models.CharField(max_length=255, verbose_name='Название компании')
    is_active = models.BooleanField(default=True, verbose_name='Active')
    last_login = models.DateTimeField(auto_now=True, verbose_name='Last login')
    is_superuser = models.BooleanField(default=False, verbose_name='Superuser status')
    is_staff = models.BooleanField(default=False, verbose_name='Is Staff')
    registration_date = models.DateField(auto_now=True, verbose_name='Дата регистрации')

    objects = UserManager()

    class Meta:
        verbose_name = 'Работодатель'
        verbose_name_plural = 'Работодатели'
        ordering = ['-registration_date']

    def __str__(self):
        return self.username

    def __repr__(self):
        return f'CustomUser obj - {self.username}'


class UserMessage(models.Model):

    id = models.AutoField(primary_key=True, verbose_name='ID')
    sender_name = models.ForeignKey(CustomUser, verbose_name='Отправитель', on_delete=models.PROTECT, related_name='related_customuser')
    message_date = models.DateTimeField(auto_now=True, verbose_name='Дата отправки')
    read_or_not = models.BooleanField(default=False, verbose_name='Прочитано')
    title = models.CharField(max_length=255, verbose_name='Тема сообщения', default='Без темы', null=True, blank=True)
    text = models.TextField(verbose_name='Текст Сообщения')

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
        ordering = ['-message_date']

    def __str__(self):
        return f'От "{self.sender_name}"'

    def __repr__(self):
        return f'UserMessage obg - {self.id}'


class AnonymousUser(models.Model):
    """
    Анонимные (не зарегистрированные) пользователи.
    Создаются при отправке сообщения из формы сайта.
    """

    id = models.AutoField(primary_key=True, verbose_name='ID')
    name = models.CharField(max_length=128, verbose_name='Имя отправителя')
    email = models.EmailField(max_length=255, unique=True, db_index=True, help_text='Электронная почта')
    company = models.CharField(max_length=255, verbose_name='Компания пользователя', null=True, blank=True, help_text='Не обязательно')
    phone = models.CharField(max_length=50, verbose_name='Телефон', null=True, blank=True, help_text='Не обязательно')
    creation_date = models.DateTimeField(auto_now=True, verbose_name='Дата создания')
    message = models.ForeignKey('AnonymousMessage', null=True, blank=True, verbose_name='Сообщения пользователя', on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Анонимный пользователь'
        verbose_name_plural = 'Анонимные пользователи'
        ordering = ['-creation_date']

    def __str__(self):
        return self.name


class AnonymousMessage(models.Model):
    """
    Сообщения от Анонимных (не зарегистрированных) пользователей.
    """

    id = models.AutoField(primary_key=True, verbose_name='ID')
    creation_date = models.DateTimeField(auto_now=True, verbose_name='Отправлено')
    sender = models.ForeignKey(AnonymousUser, verbose_name='Отправитель', on_delete=models.PROTECT)
    message_text = models.TextField(verbose_name='Текст сообщения')

    class Meta:

        verbose_name = 'Сообщение анонима'
        verbose_name_plural = 'Сообщения анонимов'
        ordering = ['-creation_date']

    def __str__(self):
        return f'От - {self.sender.name}'
