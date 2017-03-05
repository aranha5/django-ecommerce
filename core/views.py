from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import View, TemplateView

from .forms import ContactForm

class IndexView(TemplateView):

    template_name = 'index.html'


index = IndexView.as_view()

def contact(request):
    success = False
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.send_mail()
        success = True
        form = ContactForm()
    context = {
        'form': form,
        'success': success
    }
    return render(request, 'contact.html', context)
