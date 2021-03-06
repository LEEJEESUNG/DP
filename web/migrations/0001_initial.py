# Generated by Django 2.0.1 on 2018-06-15 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Node',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.TextField()),
                ('visible', models.IntegerField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='relation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_node_id', models.IntegerField()),
                ('to_node_id', models.IntegerField()),
            ],
        ),
    ]
