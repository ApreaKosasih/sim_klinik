from django.contrib import admin
from .models import Pendaftaran, User, RekamMedik

# Register your models here.

admin.site.register(Pendaftaran)
admin.site.register(User)
admin.site.register(RekamMedik)
