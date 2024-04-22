from django.urls import path
from apps.contacts.views import contact_page

urlpatterns = [
    path('', contact_page, name='contact-page'),
]
