# Generated by Django 3.2.4 on 2021-06-16 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tmapi', '0002_auto_20210616_1930'),
    ]

    operations = [
        migrations.AddField(
            model_name='venue',
            name='cell',
            field=models.CharField(default='123-123-1234', max_length=100),
            preserve_default=False,
        ),
    ]
