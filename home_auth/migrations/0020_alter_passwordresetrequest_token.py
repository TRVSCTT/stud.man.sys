# Generated by Django 5.1.1 on 2025-03-25 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_auth', '0019_alter_passwordresetrequest_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passwordresetrequest',
            name='token',
            field=models.CharField(default='j7Wt5gRu0iz46tDDzjqyyIZ47ENXZueN', editable=False, max_length=32, unique=True),
        ),
    ]
