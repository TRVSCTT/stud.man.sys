# Generated by Django 5.1.1 on 2025-03-21 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_auth', '0014_alter_passwordresetrequest_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passwordresetrequest',
            name='token',
            field=models.CharField(default='BcorZGXibOqze6a2bcbnp2kGQMVkO5PO', editable=False, max_length=32, unique=True),
        ),
    ]
