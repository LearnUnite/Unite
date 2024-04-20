# Generated by Django 5.0.4 on 2024-04-12 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Physics_Form5',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(upload_to='pics')),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField(max_length=200)),
                ('notes', models.FileField(upload_to='')),
            ],
        ),
    ]