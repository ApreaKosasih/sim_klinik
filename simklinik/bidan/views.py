import datetime
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib import messages
from .models import Pendaftaran
from django.views.generic import ListView
from django.template import Context
from django.template.loader import render_to_string, get_template
from .forms import RegisterForm, LoginForm

from django.contrib.auth import authenticate, login

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


def register(request):
    msg = None
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'user created'
            return redirect('login')
        else:
            msg = 'Terjadi Kesalahan'

    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form, 'msg': msg})


def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                msg = 'Terjadi Kesalahan'
        else:
            msg = 'Error'
    return render(request, 'login.html', {'form': form, 'msg': msg})


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


class ManagePendaftaranTemplateView(ListView):
    template_name = 'listpendaftar.html'
    model = Pendaftaran
    context_object_name = "pendaftaran"
    login_required = True
    paginate_by = 3

    def post(self, request):
        date = request.POST.get("date")
        id_pendaftaran = request.POST.get("pendaftaran-id")

        pendaftaran = Pendaftaran.objects.get(
            id=id_pendaftaran,
        )
        pendaftaran.daftar_konfirmasi = True
        pendaftaran.tanggal_konfirmasi = datetime.datetime.now()
        pendaftaran.save()

        data = {
            "name": pendaftaran.name,
            "date": date
        }
        message = get_template('email.html').render(data)
        email = EmailMessage(
            "Pendaftaran di Klinik Bidan",
            message,
            settings.EMAIL_HOST_USER,
            [pendaftaran.email]
        )
        email.content_subtype = "html"
        email.send()

        messages.add_message(request, messages.SUCCESS, f"{date}")
        return HttpResponseRedirect(request.path)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        # pendaftaran = Pendaftaran.objects.all()
        context.update({
            "title": "Manage Pendaftaran"
        })
        return context
