# Generated by Django 2.0.1 on 2018-06-15 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Similarity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('node_id', models.IntegerField(null=True)),
                ('tag_id', models.IntegerField(null=True)),
                ('importance', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='relation',
            name='importance',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='relation',
            name='interval',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='node',
            name='data',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='node',
            name='visible',
            field=models.IntegerField(default=0, max_length=4),
        ),
        migrations.AlterField(
            model_name='relation',
            name='from_node_id',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='relation',
            name='to_node_id',
            field=models.IntegerField(null=True),
        ),
        migrations.AddIndex(
            model_name='relation',
            index=models.Index(fields=['from_node_id', 'to_node_id'], name='web_relatio_from_no_3bafe5_idx'),
        ),
        migrations.AddIndex(
            model_name='similarity',
            index=models.Index(fields=['node_id', 'tag_id'], name='web_similar_node_id_311dad_idx'),
        ),
    ]
