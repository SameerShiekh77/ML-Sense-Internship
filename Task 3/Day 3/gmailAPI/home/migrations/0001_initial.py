# Generated by Django 3.2.4 on 2021-10-02 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.CharField(default='', max_length=30)),
                ('pswd', models.CharField(default='', max_length=20)),
            ],
        ),
    ]
