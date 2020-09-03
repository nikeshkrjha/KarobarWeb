# Generated by Django 3.1 on 2020-09-03 04:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('karobar', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_title', models.CharField(max_length=200, verbose_name='Title')),
                ('transaction_date', models.DateTimeField(auto_now_add=True, verbose_name='Date')),
                ('transaction_amount', models.DecimalField(decimal_places=2, max_digits=12, verbose_name='Amount')),
                ('transaction_is_cash', models.BooleanField(default=True, verbose_name='Cash')),
            ],
        ),
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_title', models.CharField(max_length=200, verbose_name='Title')),
                ('transaction_date', models.DateTimeField(auto_now_add=True, verbose_name='Date')),
                ('transaction_amount', models.DecimalField(decimal_places=2, max_digits=12, verbose_name='Amount')),
                ('transaction_is_cash', models.BooleanField(default=True, verbose_name='Cash')),
                ('sold_to', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='karobar.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supplier_name', models.CharField(max_length=100)),
                ('email', models.EmailField(blank=True, max_length=50, verbose_name='Email')),
                ('phone_number', models.CharField(max_length=13, verbose_name='Phone Number')),
                ('supplier_city', models.CharField(max_length=50, verbose_name='City')),
                ('supplier_zipcode', models.CharField(blank=True, max_length=5, verbose_name='Zip Code')),
            ],
        ),
        migrations.DeleteModel(
            name='Transaction',
        ),
        migrations.AddField(
            model_name='purchase',
            name='purchased_from',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='karobar.supplier'),
        ),
    ]