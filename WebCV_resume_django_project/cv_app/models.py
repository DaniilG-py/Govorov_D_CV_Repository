from django.db import models
from django.contrib.auth.models import (
                                        AbstractUser,
                                        BaseUserManager,
                                    )


class WorkingExperience(models.Model):
    """
    Информация об опыте работы
    """

    company_name = models.CharField(max_length=255, verbose_name='Место работы')
    position = models.CharField(max_length=300, verbose_name='Должность')
    start_date = models.DateField(verbose_name='Начало работы')
    end_date = models.DateField(
            verbose_name='Окончание работы',
            null=True,
            blank=True,
            help_text='Оставьте поле пустым чтобы получить значение "По настоящее время"',
        )
    responsibilities = models.TextField(verbose_name='Описание обязанностей')
    company_web_address = models.CharField(max_length=100, verbose_name='Сайт компании', null=True, blank=True)

    def __str__(self):
        return f'{self.position} - {self.company_name}'

    class Meta:
        verbose_name = 'Опыт работы'
        verbose_name_plural = 'Опыт работы'
        ordering = ['-start_date']


class EducationExperience(models.Model):
    """
    Информация об обучении
    """
    GRAD_YEARS = (
            '2013',
            '2014',
            '2015',
            '2016',
            '2017',
            '2018',
            '2019',
            '2020',
            '2021',
        )
    HIGHER_EDUCATION = 'Высшее образование'
    COURSE = 'Курсы'

    GRAD_YEAR_CHOICE = (
            (GRAD_YEARS[0], '2013'),
            (GRAD_YEARS[1], '2014'),
            (GRAD_YEARS[2], '2015'),
            (GRAD_YEARS[3], '2016'),
            (GRAD_YEARS[4], '2017'),
            (GRAD_YEARS[5], '2018'),
            (GRAD_YEARS[6], '2019'),
            (GRAD_YEARS[7], '2020'),
            (GRAD_YEARS[8], '2021'),
        )

    CATEGORY_CHOICE = (
            (HIGHER_EDUCATION, 'Высшее образование'),
            (COURSE, 'Повышение квалификации, курсы'),
        )

    grad_year = models.CharField(max_length=4, choices=GRAD_YEAR_CHOICE, verbose_name='Год окончания')
    category = models.CharField(max_length=255, choices=CATEGORY_CHOICE, verbose_name='Тип обучения')
    place = models.CharField(max_length=255, verbose_name="Место обучения")
    description = models.TextField(null=True, blank=True, verbose_name="Описание")

    class Meta:
        verbose_name = 'Образование'
        verbose_name_plural = 'Образование'
        ordering = ['-grad_year']

    def __str__(self):
        return self.place


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


class AnonymousUser(models.Model):
    """
    Анонимные (не зарегистрированные) пользователи.
    Создаются при отправке сообщения из формы сайта.
    """

    name = models.CharField(max_length=128, verbose_name='Имя')
    email = models.EmailField(max_length=255, unique=False, db_index=True, verbose_name='Электронная почта')
    company = models.CharField(max_length=255, verbose_name='Компания', null=True, blank=True)
    phone = models.CharField(max_length=50, verbose_name='Телефон', null=True, blank=True)
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

    creation_date = models.DateTimeField(auto_now=True, verbose_name='Отправлено')
    subject = models.CharField(max_length=255, verbose_name='Тема письма', null=True, blank=True)
    sender = models.ForeignKey(AnonymousUser, null=True, blank=True, verbose_name='Отправитель', on_delete=models.PROTECT)
    message_text = models.TextField(verbose_name='Текст сообщения')

    class Meta:

        verbose_name = 'Сообщение анонима'
        verbose_name_plural = 'Сообщения анонимов'
        ordering = ['-creation_date']

    def __str__(self):
        return f'От - {self.sender.name}'
