from django.shortcuts import render
from .forms import ContactForm
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.template import Context
from django.contrib import messages

def contact(request):
    form_class = ContactForm

    if request.method == 'POST':
        form = form_class(data=request.POST)

        # Validate account.
        if form.is_valid():
            contact_name = request.POST.get('contact_name', '')
            contact_email = request.POST.get('contact_email', '')
            contact_subject = request.POST.get('contact_subject', '')
            form_content = request.POST.get('content', '')

            # Create content.
            template = get_template('contact_template.txt')
            context = Context({
                'contact_name': contact_name,
                'contact_email': contact_email,
                'contact_subject': contact_subject,
                'form_content': form_content,
            })
            content = template.render(context)

            # Set email contents and send.
            email = EmailMessage("New Message at evklein.com", content,
            "http://www.evklein.com/", ['evklein.com@gmail.com'], headers =
             {'Reply-To': contact_email })

            email.send()

            # Send success message!
            messages.add_message(request, messages.SUCCESS, 'Message successfully delivered.')

        # Deliver failure message if form is invalid.
        else:
            messages.add_message(request, messages.ERROR, 'Message failed to deliver. Please make sure all information is correct.')

    return render(request, 'contact.html', { 'form': form_class })
