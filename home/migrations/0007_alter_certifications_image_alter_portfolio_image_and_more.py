# Generated by Django 4.1 on 2022-10-30 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_alter_certifications_image_alter_portfolio_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certifications',
            name='image',
            field=models.URLField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='image',
            field=models.URLField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.URLField(max_length=1000),
        ),
    ]
