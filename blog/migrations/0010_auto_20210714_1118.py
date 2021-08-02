# Generated by Django 3.2.4 on 2021-07-14 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20210714_1026'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='work_year',
            field=models.CharField(default='ss', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='project',
            name='project_type',
            field=models.IntegerField(choices=[(0, 'Game Development'), (1, 'Web Development'), (2, 'Web Design'), (3, 'UI/UX'), (4, 'API'), (5, 'Web Slicing')], default=0),
        ),
    ]
