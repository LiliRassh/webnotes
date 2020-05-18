# Generated by Django 3.0.6 on 2020-05-14 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=100)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('for_who', models.CharField(max_length=100)),
                ('craft', models.CharField(max_length=100)),
                ('image', models.FileField(upload_to='upload/')),
                ('note', models.TextField(max_length=512)),
            ],
        ),
    ]
