# Generated by Django 3.0 on 2019-12-20 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku', models.CharField(max_length=200)),
                ('p_tittle', models.CharField(max_length=200)),
                ('img_url', models.CharField(max_length=2000)),
                ('p_description', models.TextField()),
                ('p_price', models.CharField(max_length=50)),
            ],
        ),
    ]
