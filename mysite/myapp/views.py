from django.shortcuts import render
from django.contrib.auth import login
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView, TemplateView
from .mixins import RequestToFormKwargsMixin, PkToFormKwargsMixin, AdminPassTestMixin
from .models import Reservation, Play, Carousel, Feedback
from .forms import ReservationForm, ReservationWithPlayForm, FeedbackForm
from django.urls import reverse_lazy

class CreateReservationView(PkToFormKwargsMixin, CreateView):
    model = Reservation
    form_class = ReservationForm
    template_name = 'forms/reservation.html'
    success_url = '/'


class MainPageView(TemplateView):
    template_name = "web/main.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["carousel_images"] = Carousel.objects.all()
        context["plays"] = (
            Play.objects.filter().order_by("date")[:3]               
        )
        return context

class ContactsPageView(TemplateView):
    template_name = "web/contacts.html"

class AboutUsPageView(ListView):
    model = Carousel
    context_object_name = "carousel_images"
    template_name = "web/about_us.html"

class PartnersPageView(TemplateView):
    template_name = "web/partners.html"

class ProgramPageView(ListView):
    model = Play
    template_name = "web/program.html"
    context_object_name = "plays"

class TicketsPageView(CreateView):
    template_name = "forms/tickets.html"
    model = Reservation
    form_class = ReservationWithPlayForm
    success_url = "/"


class PlayView(DetailView):
    template_name = "web/play.html"
    model = Play
    context_object_name = "play"


class FeedbackPageView(CreateView):
    template_name = "forms/feedback.html"
    model = Feedback
    form_class = FeedbackForm
    success_url = "/"