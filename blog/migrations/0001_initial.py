# Generated by Django 3.2 on 2021-05-05 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=24)),
                ('description', models.TextField(max_length=128)),
                ('post_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
