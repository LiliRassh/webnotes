# Generated by Django 3.0.6 on 2020-05-31 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webnotes', '0011_auto_20200531_1044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='webnote',
            name='create_date',
            field=models.DateTimeField(default='2020-05-31 14:24:53'),
        ),
        migrations.AlterField(
            model_name='webnote',
            name='image',
            field=models.FileField(null=True, upload_to='upload/webnotes'),
        ),
    ]
