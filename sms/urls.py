from django.urls import path

from .views import send_code_api_view

urlpatterns = [
    path('send/', send_code_api_view, name='send_code'),
]
