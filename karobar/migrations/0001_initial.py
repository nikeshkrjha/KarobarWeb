# Generated by Django 3.1 on 2020-09-02 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_fname', models.CharField(max_length=50, verbose_name='First Name')),
                ('customer_lname', models.CharField(max_length=50, verbose_name='Last Name')),
                ('email', models.EmailField(blank=True, max_length=50, verbose_name='Email')),
                ('phone_number', models.CharField(max_length=13, verbose_name='Phone Number')),
                ('customer_city', models.CharField(max_length=50, verbose_name='City')),
                ('customer_zipcode', models.CharField(blank=True, max_length=5, verbose_name='Zip code')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_title', models.CharField(max_length=200, verbose_name='Title')),
                ('transaction_date', models.DateTimeField(auto_now_add=True, verbose_name='Date')),
                ('transaction_amount', models.DecimalField(decimal_places=2, max_digits=12, verbose_name='Amount')),
                ('transaction_is_cash', models.BooleanField(default=True, verbose_name='Cash')),
            ],
        ),
    ]
