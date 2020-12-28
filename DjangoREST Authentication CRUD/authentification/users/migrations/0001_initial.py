# Generated by Django 3.1.4 on 2020-12-28 19:33

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
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=150, unique='True', verbose_name='Username')),
                ('password', models.CharField(max_length=128, verbose_name='Password')),
                ('first_name', models.CharField(max_length=30, verbose_name='First name')),
                ('last_name', models.CharField(max_length=150, verbose_name='Last name')),
                ('is_active', models.BooleanField(default=False, verbose_name='Active')),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='Last login')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='Superuser status')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
        ),
    ]
