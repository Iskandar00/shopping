from django.urls import path
from apps.users.views import register, send_code_to_email, register_user, login_page, log_out

urlpatterns = [
    path('', register, name='register-page'),
    path('send_email_to_user', send_code_to_email, name='send_email_to_user-page'),
    path('register_user/', register_user, name='register_user-page'),
    path('login_page/', login_page, name='login-page'),
    path('log_out/', log_out, name='log_out-page')
]