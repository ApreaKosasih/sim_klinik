from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    is_admin = models.BooleanField('is admin', default=False)
    is_customer = models.BooleanField('is customer', default=False)
    is_bidan = models.BooleanField('is bidan', default=False)


class Pendaftaran(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    nomortelepon = models.CharField(max_length=15)
    jeniskelamin = models.CharField(max_length=15)
    message = models.TextField(blank=True)
    tanggal_daftar = models.DateField(auto_now_add=True)
    daftar_konfirmasi = models.BooleanField(default=False)
    periksa_konfirmasi = models.BooleanField(default=False)
    tanggal_konfirmasi = models.DateField(
        auto_now_add=False, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["tanggal_konfirmasi", ]


class RekamMedik(models.Model):
    pasien = models.ForeignKey(
        Pendaftaran,
        on_delete=models.CASCADE
    )
    tanggal_periksa = models.DateField(auto_now_add=True)
    message = models.TextField(blank=True)
    status = models.BooleanField(default=False)
    tanggal_kembali = models.DateField(
        auto_now_add=False, null=True, blank=True)
