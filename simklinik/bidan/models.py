from django.db import models

# Create your models here.


class Pendaftaran(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    nomortelepon = models.CharField(max_length=15)
    jeniskelamin = models.CharField(max_length=15)
    message = models.TextField(blank=True)
    tanggal_daftar = models.DateField(auto_now_add=True)
    daftar_konfirmasi = models.BooleanField(default=False)
    tanggal_konfirmasi = models.DateField(
        auto_now_add=False, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-tanggal_daftar", ]