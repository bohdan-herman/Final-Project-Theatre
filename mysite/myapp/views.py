from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.shortcuts import redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .mixins import RequestToFormKwargsMixin
from .models import Reservation
from .forms import ReservationForm


class StaffLoginView(LoginView):
    template_name = 'staff/login.html'

    def form_valid(self, form):
        user = form.get_user()
        if user.is_staff:
            login(self.request, user)
            return redirect('admin_panel')

class ReservationView(RequestToFormKwargsMixin, CreateView):
    model = Reservation
    form_class = ReservationForm
    template_name = 'reservation.html'
    success_url = 'email_send/'

