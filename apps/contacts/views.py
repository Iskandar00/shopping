from django.shortcuts import render, redirect
from django.contrib import messages

from apps.contacts.models import Contact


def contact_page(request):
    if request.method != 'POST':
        return render(request, 'contact.html')

    user = request.user

    name = request.POST.get('name')
    email = request.POST.get('email')
    subject = request.POST.get('subject')
    message = request.POST.get('message')

    if request.user.is_authenticated:
        name = user.first_name
        email = user.email
    elif not (email and name):
        messages.error(request, 'name yoki email kiritilmadi!!!')
        return redirect('contact-page')
    Contact.objects.create(name=name, email=email, message=message, title=subject)
    messages.success(request, 'Success send')
    return redirect('contact-page')
