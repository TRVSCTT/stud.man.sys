# Generated by Django 5.1.1 on 2025-03-24 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_auth', '0015_alter_passwordresetrequest_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passwordresetrequest',
            name='token',
            field=models.CharField(default='LlunSihQzbidVh3Bo7Fv2F06uP9GeItE', editable=False, max_length=32, unique=True),
        ),
    ]
