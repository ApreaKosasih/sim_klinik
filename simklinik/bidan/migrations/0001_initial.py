# Generated by Django 3.2.16 on 2022-11-09 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pendaftaran',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=100)),
                ('nomortelepon', models.CharField(max_length=15)),
                ('jeniskelamin', models.CharField(max_length=15)),
                ('message', models.TextField(blank=True)),
                ('tanggal_daftar', models.DateField(auto_now_add=True)),
                ('daftar_konfirmasi', models.BooleanField(default=False)),
                ('tanggal_konfirmasi', models.DateField()),
            ],
            options={
                'ordering': ['-tanggal_daftar'],
            },
        ),
    ]
