# Generated by Django 3.2.4 on 2021-06-25 10:13

from django.db import migrations, models
from django.utils import timezone

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(default='', max_length=100, null=True)),
                ('Age', models.IntegerField(default=1, null=True)),
                ('Pub_Date', models.DateTimeField(default=timezone.now, null=True)),
                ('Email', models.EmailField(default='', max_length=254, null=True)),
                ('Introduce', models.TextField(null=True)),
                ('Image', models.ImageField(null=True, upload_to='')),
            ],
        ),
    ]
