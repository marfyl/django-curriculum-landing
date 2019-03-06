from django.conf import settings
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic.edit import FormView

from .forms import ContactForm


class LandingView(SuccessMessageMixin, FormView):
    template_name = 'landing/index.html'
    form_class = ContactForm
    success_url = reverse_lazy('landing:index')
    success_message = 'Thank you for getting in touch! Your message has been sent.'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['ANALYTICS_CODE'] = settings.ANALYTICS_CODE
        return context

    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)
