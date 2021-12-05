# Generated by Django 3.1.7 on 2021-04-14 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anonymoususer',
            name='company',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Компания'),
        ),
        migrations.AlterField(
            model_name='anonymoususer',
            name='email',
            field=models.EmailField(db_index=True, max_length=255, verbose_name='Электронная почта'),
        ),
        migrations.AlterField(
            model_name='anonymoususer',
            name='name',
            field=models.CharField(max_length=128, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='anonymoususer',
            name='phone',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Телефон'),
        ),
    ]
