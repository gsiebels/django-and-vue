# Generated by Django 3.0.3 on 2020-02-12 15:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hairdresser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('about', models.CharField(max_length=200)),
                ('image', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=500)),
                ('prices', models.IntegerField(default=0)),
                ('hairdresser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hairdresser.Hairdresser')),
            ],
        ),
    ]
