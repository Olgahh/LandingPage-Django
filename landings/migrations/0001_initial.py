# Generated by Django 3.1.5 on 2021-01-15 17:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_lifecycle.mixins


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BasicInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('about', models.TextField(blank=True)),
                ('location', models.CharField(max_length=120)),
                ('phone_number', models.CharField(max_length=12)),
            ],
            options={
                'verbose_name_plural': 'Basic Info',
            },
        ),
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
            options={
                'verbose_name_plural': 'Detailed Information',
            },
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='')),
                ('basic_information', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='landings.basicinfo')),
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            bases=(django_lifecycle.mixins.LifecycleModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='landings.organization')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            bases=(django_lifecycle.mixins.LifecycleModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subtitle', models.CharField(blank=True, max_length=120)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('text', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='landings.info')),
            ],
        ),
        migrations.AddField(
            model_name='basicinfo',
            name='details',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='landings.detail'),
        ),
    ]
