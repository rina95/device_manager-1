# Generated by Django 3.0.3 on 2020-02-28 14:31

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, verbose_name='Full Name')),
                ('code', models.CharField(max_length=50, unique=True, verbose_name='Employee Code')),
                ('is_staff', models.BooleanField(default=False, verbose_name='staff status')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='superuser status')),
                ('is_active', models.BooleanField(default=True, verbose_name='active')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='date created')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='date updated')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]