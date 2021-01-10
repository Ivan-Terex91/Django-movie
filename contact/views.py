from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import CreateView, UpdateView

from .models import Contact
from .forms import ContactForm
from .service import send_email


class ContactView(CreateView):
    model = Contact
    form_class = ContactForm
    success_url = "/"

    def form_valid(self, form):
        if not Contact.objects.filter(email=form.instance.email).exists():
            form.save()
            send_email(form.instance.email)
            return super().form_valid(form)
        return HttpResponseRedirect(self.success_url)