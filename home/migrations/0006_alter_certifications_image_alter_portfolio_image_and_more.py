# Generated by Django 4.1 on 2022-10-30 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_order_prize_alter_order_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certifications',
            name='image',
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='image',
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.URLField(),
        ),
    ]
