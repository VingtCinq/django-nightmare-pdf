import os
from django.shortcuts import render
from .settings import pdf_settings


def pdf_html(request, html_key):
	filename = '%s.html' % html_key
	response = render(request, 'nightmare_pdf/%s' % filename)
	os.remove(os.path.join(pdf_settings.TEMPLATES_DIR, filename))
	return response