# Generated by Django 5.1.1 on 2024-12-13 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('price', models.FloatField(default=0.0)),
                ('edition', models.SmallIntegerField(default=1)),
                ('author', models.CharField(max_length=50)),
            ],
        ),
    ]
