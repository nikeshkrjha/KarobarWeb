# Generated by Django 3.1 on 2020-09-03 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('karobar', '0003_paymentsreceived_supplierpayment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymentsreceived',
            name='payment_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='supplierpayment',
            name='payment_date',
            field=models.DateTimeField(),
        ),
    ]
