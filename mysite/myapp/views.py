from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView, TemplateView
from .mixins import RequestToFormKwargsMixin, PkToFormKwargsMixin, AdminPassTestMixin
from .models import Reservation, Play, Carousel
from .forms import ReservationForm, PlayForm,CarouselForm
from django.urls import reverse_lazy
from django.utils import timezone

class CreateReservationView(PkToFormKwargsMixin, CreateView):
    model = Reservation
    form_class = ReservationForm
    template_name = 'reservation.html'
    success_url = '/'


class DeletePlayView(AdminPassTestMixin, DeleteView):
    model = Play
    success_url = '/'


class UpdatePlayView(AdminPassTestMixin, UpdateView):
    model = Play
    form_class = PlayForm
    template_name = 'staff/play/update_play.html'
    success_url = '/'


class CreatePlayView(AdminPassTestMixin, CreateView):
    model = Play
    form_class = PlayForm
    template_name = 'staff/play/create_play.html'
    success_url = '/'


class DeleteCarouselView(AdminPassTestMixin, DeleteView):
    model = Carousel
    success_url = '/'


class UpdateCarouselView(AdminPassTestMixin, UpdateView):
    model = Carousel
    form_class = CarouselForm
    template_name = 'staff/carousel/update_carousel.html'
    success_url = '/'


class CreateCarouselView(AdminPassTestMixin, CreateView):
    model = Carousel
    form_class = CarouselForm
    template_name = 'staff/carousel/create_carousel.html'
    success_url = '/'

class MainPageView(TemplateView):
    template_name = "web/main.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        now = timezone.now()
        context["carousel_images"] = Carousel.objects.all()
        context["plays"] = (
            Play.objects.filter(date__gte=now).order_by("date")[:3]               
        )
        return context

class ContactsPageView(TemplateView):
    template_name = "web/contacts.html"

class AboutUsPageView(TemplateView):
    template_name = "web/about_us.html"

class PartnersPageView(TemplateView):
    template_name = "web/partners.html"

class ProgramPageView(ListView):
    model = Play
    template_name = "web/program.html"

class TicketsPageView(TemplateView):
    template_name = "web/tickets.html"

class PlayView(DetailView):
    template_name = "web/play.html"
    model = Play