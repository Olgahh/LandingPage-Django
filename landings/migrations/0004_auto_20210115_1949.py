# Generated by Django 3.1.5 on 2021-01-15 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landings', '0003_organization_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]