# Generated by Django 4.1 on 2022-09-03 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=200)),
                ('Phone', models.CharField(max_length=50)),
                ('contact', models.TextField()),
            ],
        ),
    ]
