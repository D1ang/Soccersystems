from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.template.loader import get_template
from django.contrib import messages

from django.core.mail import EmailMessage
from home.forms import ContactForm


def index(request):
    """
    Load the homepage if there is
    no POST request. if POST load the data
    and send an email with office365 smtp.
    """
    form = ContactForm

    if request.method == 'POST':
        form = form(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get('contact_name', '')
            contact_email = request.POST.get('contact_email', '')
            form_content = request.POST.get('content', '')

            # Create the email on the contact template
            template = get_template('contact.html')
            context = {
                'contact_name': contact_name,
                'contact_email': contact_email,
                'form_content': form_content
            }
            content = template.render(context)

            email = EmailMessage(
                "Soccersystems bericht",
                content,
                "info@ibsgraphics.nl" + '', ['info@ibsgraphics.nl'],
                headers={'Reply-To': contact_email}
            )
            email.send()
            messages.success(request, 'Bericht is succesvol verzonden!')
            return HttpResponseRedirect('/')

    return render(request, 'home/index.html', {
        'form': form,
    })
