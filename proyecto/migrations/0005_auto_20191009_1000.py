# Generated by Django 2.2.6 on 2019-10-09 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyecto', '0004_auto_20191009_0928'),
    ]

    operations = [
        migrations.CreateModel(
            name='imagen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='projects')),
            ],
        ),
        migrations.AddField(
            model_name='proyecto',
            name='imagen',
            field=models.ManyToManyField(to='proyecto.imagen'),
        ),
    ]
