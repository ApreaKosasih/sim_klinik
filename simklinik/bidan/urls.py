from django.urls import path
from .views import HomeTemplateView, TentangTemplateView, PendaftaranTemplateView, BidanTemplateView, ManagePendaftaranTemplateView
from . import views

urlpatterns = [
    path('', HomeTemplateView.as_view(), name='home'),
    path('tentang-aplikasi/', TentangTemplateView.as_view(), name='tentang'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('pendaftaran/', PendaftaranTemplateView.as_view(), name='pendaftaran'),
    path('bidan/', BidanTemplateView.as_view(), name='bidan'),
    path('managependaftaran/', ManagePendaftaranTemplateView.as_view(), name='manage'),
]
