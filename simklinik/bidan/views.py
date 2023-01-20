from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib import messages
from .models import Pendaftaran
# Create your views here.


class HomeTemplateView(TemplateView):
    template_name = 'index.html'

    def post(self, request):
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        email = EmailMessage(
            subject=f"{name} pendaftaran klinik bidan.",
            body=message,
            from_email=settings.EMAIL_HOST_USER,
            to=[settings.EMAIL_HOST_USER],
            reply_to=[email]
        )

        email.send()
        messages.add_message(request, messages.SUCCESS,
                             f"Terimakasih {name} telah menghubungi kami, email anda berhasil terkirim..")
        return HttpResponseRedirect(request.path)
        # return HttpResponse('Email telah sukses terkirim, silahkan tunggu admin kami akan segera membalas pesan anda...')


class PendaftaranTemplateView(TemplateView):
    template_name = 'pendaftaran.html'

    def post(self, request):
        name = request.POST.get("name")
        nomortelepon = request.POST.get("nomortelepon")
        email = request.POST.get("email")
        jeniskelamin = request.POST.get("jeniskelamin")
        message = request.POST.get("message")

        pendaftaran = Pendaftaran.objects.create(
            name=name,
            email=email,
            nomortelepon=nomortelepon,
            message=message,
            jeniskelamin=jeniskelamin,
        )

        pendaftaran.save()

        messages.add_message(request, messages.SUCCESS,
                             f"Terimaksih, {name} untuk proses pendaftaran sudah berhasil...")
        return HttpResponseRedirect(request.path)


class ManagePendaftaranTemplateView(TemplateView):
    template_name = 'listpendaftar.html'
    login_required = True

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        pendaftaran = Pendaftaran.objects.all()
        context.update({
            "pendaftaran": pendaftaran,
            "title": "Manage Pendaftaran"
        })
        return context


# class ManagePendaftaranTemplateView(ListView):
#     template_name = 'listpendaftar.html'
#     model = Pendaftaran
#     context_object_name = "pendaftaran"
#     login_required = True
#     paginate_by = 5

#     def get_context_data(self, *args, **kwargs):
#         context = super().get_context_data(*args, **kwargs)
#         pendaftaran = Pendaftaran.objects.all()
#         context.update({
#             "title": "Manage Pendaftaran"
#         })
#         return context
