# Generated by Django 4.2.13 on 2024-06-07 06:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_unit'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='unit',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.unit'),
        ),
    ]