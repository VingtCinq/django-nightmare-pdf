from django.contrib import admin
from .models import PdfDoc


class PdfDocAdmin(admin.ModelAdmin):
    list_display = ('document', 'title', 'description',)

admin.site.register(PdfDoc, PdfDocAdmin)
