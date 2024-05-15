from django.urls import path
from apps.comments.views import comment_create

urlpatterns = [
    path('<int:pk>/', comment_create, name='comment_create-page'),
]
