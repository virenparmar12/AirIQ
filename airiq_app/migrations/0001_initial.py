# Generated by Django 3.2.3 on 2021-05-25 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CopperSilver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_material', models.CharField(max_length=20)),
                ('amo', models.IntegerField()),
                ('corrosion_rate', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='HomeData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('differential_pressure', models.FloatField()),
                ('temprature', models.IntegerField()),
                ('relative_humidity', models.IntegerField()),
                ('metal_loss1', models.IntegerField()),
                ('metal_loss2', models.IntegerField()),
                ('cr1', models.IntegerField()),
                ('cr2', models.IntegerField()),
                ('corrosion_rate1', models.CharField(max_length=5)),
                ('corrosion_rate2', models.CharField(max_length=5)),
            ],
        ),
    ]
