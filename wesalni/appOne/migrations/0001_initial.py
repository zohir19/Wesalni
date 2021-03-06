# Generated by Django 2.1.5 on 2019-02-06 22:17

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('date_of_birth', models.DateField()),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, unique=True)),
                ('city', models.CharField(max_length=50)),
            ],
        ),
    ]
