# Generated by Django 3.1.3 on 2021-01-14 20:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('consumptions', '0002_auto_20201124_1434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consumption',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='consumptions.product'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='consumptions.product_category'),
        ),
    ]
