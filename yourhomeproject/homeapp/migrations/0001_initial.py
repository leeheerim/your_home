# Generated by Django 4.1.2 on 2022-11-13 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('번호', models.FloatField()),
                ('주택관리번호', models.FloatField()),
                ('공고번호', models.FloatField()),
                ('주택명', models.CharField(max_length=20)),
                ('위도', models.FloatField()),
                ('경도', models.FloatField()),
                ('공급위치', models.CharField(max_length=30)),
            ],
        ),
    ]
