from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _
from nightmare_pdf.settings import pdf_settings


class PdfDoc(models.Model):
	"""
	Store each generated pdf
	"""
	title = models.CharField(verbose_name=_("Title"), max_length=255, blank=True)
	description = models.TextField(verbose_name=_("Description"), blank=True)
	document = models.FileField(verbose_name=_("Document PDF"), upload_to=pdf_settings.UPLOAD_TO)
	created_at = models.DateTimeField(auto_now=False, auto_now_add=True, verbose_name=_('Creation'))
	updated_at = models.DateTimeField(auto_now=True, auto_now_add=False, verbose_name=_('Update'))

	def __unicode__(self):
		return self.document.name

	class Meta:
		verbose_name = 'PDF Document'
		verbose_name_plural = 'PDF Documents'
		ordering = ['-created_at']