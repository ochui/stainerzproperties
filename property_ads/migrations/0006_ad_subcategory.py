# Generated by Django 3.0.2 on 2020-02-14 23:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('property_ads', '0005_auto_20200215_0036'),
    ]

    operations = [
        migrations.AddField(
            model_name='ad',
            name='subcategory',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='subcategory', to='property_ads.Category'),
        ),
    ]
