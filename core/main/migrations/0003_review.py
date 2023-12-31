# Generated by Django 4.2.5 on 2023-09-14 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_notebook_about'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, verbose_name='Review user email')),
                ('phone', models.CharField(max_length=100, verbose_name='Review user phone number')),
                ('text', models.TextField(verbose_name='Review user text')),
            ],
        ),
    ]
