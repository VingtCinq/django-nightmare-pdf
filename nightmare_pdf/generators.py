import subprocess
import os
import random
from django.core.validators import URLValidator
from nightmare_pdf.settings import pdf_settings
from django.http import (
	HttpResponse,
	Http404
)
from django.core.files.base import ContentFile
from .models import PdfDoc


validate_url = URLValidator(schemes=['https', 'http'])


class PDFGenerator(object):

	def __init__(self, url, timeout=1000, page_size='A4', landscape=0, 
				 print_background=1, margins_type=1, script=pdf_settings.DEFAULT_RENDER_SCRIPT,
				 temp_dir=pdf_settings.DEFAULT_TEMP_DIR):
		validate_url(url)
		self.url = url
		self.filename = self.__get_random_filename()
		self.filepath = self.__get_filepath()
		self.timeout = timeout
		self.page_size = page_size
		self.landscape = landscape
		self.print_background = print_background
		self.margins_type = margins_type
		self.script = script
		self.temp_dir = temp_dir
		self.pdf_data = None
		self.__generate()
		self.__set_pdf_data()
		self.__remove_source_file()


	def __get_random_filename(self):
		choices = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
		name = "".join([random.choice(choices) for i in range(50)])
		return "%s.pdf" % name


	def __get_filepath(self):
		return os.path.join(pdf_settings.DEFAULT_TEMP_DIR, self.filename)


	def __generate(self):
		"""
		call the following command:
			node render_pdf.js [url] [filepath] 
				--timeout [timeout]
				--pageSize [page_size]
				--landscape [landscape]
				--printBackground [print_background]
				--marginsType [margins_type]
		"""
		command = [
			pdf_settings.NODE_PATH,
			self.script,
			self.url,
			self.filepath,
			'--timeout',
			str(self.timeout),
			'--pageSize',
			self.page_size,
			'--landscape',
			str(self.landscape),
			'--printBackground',
			str(self.print_background),
			'--marginsType',
			str(self.margins_type)
		]
		return subprocess.call(command)


	def __set_pdf_data(self):
		with open(self.filepath) as pdf:
			self.pdf_data = pdf.read()


	def get_content_file(self, filename):
		return ContentFile(self.pdf_data, name=filename)


	def get_data(self):
		return self.pdf_data

	def get_http_response(self, filename):
		response = HttpResponse(self.pdf_data, content_type='application/pdf')
		response['Content-Disposition'] = 'attachment; filename="%s.pdf"' % filename
		return response


	def __remove_source_file(self):
		return subprocess.call(['rm', self.filepath])


	def save(self, filename, title='', description=''):
		file = self.get_content_file(filename)
		document = PdfDoc(
			title=title,
			description=description,
			document=file)
		document.save()
		return document


