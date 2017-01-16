# -*- coding: utf-8 -*-
import re
from django.core.management.base import BaseCommand
from nightmare_pdf.generators import PDFGenerator


class Command(BaseCommand):

    def handle(self, *args, **options):
    	pdf = PDFGenerator('http://stackoverflow.com/questions/5545160/how-can-i-use-multiple-template-files-for-a-joomla-module')
    	pdf.save('test.pdf')