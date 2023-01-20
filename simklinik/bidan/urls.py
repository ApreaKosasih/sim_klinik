from django.urls import path
from .views import HomeTemplateView, PendaftaranTemplateView, ManagePendaftaranTemplateView


urlpatterns = [
    path('', HomeTemplateView.as_view(), name='home'),
    path('pendaftaran/', PendaftaranTemplateView.as_view(), name='pendaftaran'),
    path('managependaftaran/', ManagePendaftaranTemplateView.as_view(), name='manage'),
]
