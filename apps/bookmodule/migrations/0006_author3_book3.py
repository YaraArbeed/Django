# Generated by Django 5.1.1 on 2024-12-28 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookmodule', '0005_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100)),
                ('address', models.TextField(max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Book3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('price', models.FloatField(default=0)),
                ('genre', models.CharField(max_length=50)),
                ('coverPage', models.FileField(upload_to='documents/')),
                ('authors', models.ManyToManyField(to='bookmodule.author3')),
            ],
        ),
    ]
