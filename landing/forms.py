from django import forms
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string


class ContactForm(forms.Form):
    name = forms.CharField(required=True)
    email = forms.EmailField(required=False, label='Email (optional)')
    message = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={'rows': '4'})
    )

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    def send_email(self):
        if settings.EMAIL_HOST_PASSWORD and settings.ADMIN_EMAIL:
            subject = 'Nuevo contacto en marfylaso'
            email_from = settings.EMAIL_HOST_USER
            email_to = settings.ADMIN_EMAIL
            data = {
                'name': self.cleaned_data.get('name'),
                'email': self.cleaned_data.get('email', '-'),
                'message': self.cleaned_data.get('message'),
            }
            body = render_to_string('landing/contact_email.html', data)
            send_mail(subject, body, email_from, [email_to], fail_silently=False)
