# Generated by Django 3.1.4 on 2020-12-09 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('body_text', models.TextField()),
                ('pub_date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
