# Generated by Django 5.1.1 on 2024-12-20 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookmodule', '0003_author_exambook'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Student2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.PositiveIntegerField()),
                ('addresses', models.ManyToManyField(to='bookmodule.address2')),
            ],
        ),
    ]
