# Generated by Django 5.1.1 on 2025-02-28 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_auth', '0009_alter_passwordresetrequest_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passwordresetrequest',
            name='token',
            field=models.CharField(default='1CdoRSHpxO4nC20GRRAZ8TCNx8wbSaWp', editable=False, max_length=32, unique=True),
        ),
    ]
