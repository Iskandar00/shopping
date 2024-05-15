from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from apps.orders.forms import OrderForm


@login_required
def order_create(request):
    if request.method != 'POST':
        return redirect('checkout_page')
    form = OrderForm(request.POST)
    if form.is_valid():
        form.save()
    else:
        messages.error(request, form.errors)
    return redirect('checkout-page')
