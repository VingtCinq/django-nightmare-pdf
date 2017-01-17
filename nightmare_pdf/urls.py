from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(?P<html_key>[a-zA-Z0-9]+)$', views.pdf_html, name='pdf_html'),
]