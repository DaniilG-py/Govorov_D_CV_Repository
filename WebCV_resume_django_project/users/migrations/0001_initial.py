# Generated by Django 3.1.7 on 2021-03-31 15:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(db_index=True, max_length=100, unique=True, verbose_name='Никнейм')),
                ('password', models.CharField(max_length=128, verbose_name='Пароль')),
                ('email', models.EmailField(db_index=True, help_text='Почта для связи с Вами.', max_length=255, unique=True)),
                ('first_name', models.CharField(max_length=200, verbose_name='Ваше имя')),
                ('last_name', models.CharField(max_length=200, null=True, verbose_name='Ваша фамилия')),
                ('phone', models.CharField(blank=True, max_length=20, null=True, verbose_name='Телефонный номер')),
                ('company_name', models.CharField(max_length=255, verbose_name='Название компании')),
                ('is_active', models.BooleanField(default=False, verbose_name='Active')),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='Last login')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='Superuser status')),
                ('is_staff', models.BooleanField(default=False, verbose_name='Is Staff')),
                ('registration_date', models.DateField(auto_now=True, verbose_name='Дата регистрации')),
            ],
            options={
                'verbose_name': 'Работодатель',
                'verbose_name_plural': 'Работодатели',
                'ordering': ['-registration_date'],
            },
        ),
    ]