"""
Settings for Nightmare PDF are all namespaced in the NIGHTMARE_PDF setting.
For example your project's `settings.py` file might look like this:

NIGHTMARE_PDF = {
    'UPLOAD_TO': 'pdfs',
}

This module provides the `pdf_setting` object, that is used to access
PDF settings, checking for user settings first, then falling
back to the defaults.
"""
from __future__ import unicode_literals
import os

from django.test.signals import setting_changed


NIGHTMARE_PDF_DIR = os.path.dirname(os.path.abspath(__file__))

DEFAULTS = {
    'UPLOAD_TO': 'pdfs',
    'NODE_PATH': 'node',
    'DEFAULT_RENDER_SCRIPT': os.path.join(NIGHTMARE_PDF_DIR, 'render_pdf.js'),
    'DEFAULT_TEMP_DIR': os.path.join(NIGHTMARE_PDF_DIR, 'temp'),
    'TEMPLATES_DIR': os.path.join(NIGHTMARE_PDF_DIR, 'templates/nightmare_pdf')
}


class PDFSettings(object):
    """
    A settings object, that allows PDF settings to be accessed as properties.
    For example:
        from nightmare_pdf.settings import api_settings
        print(pdf_settings.UPLOAD_TO)
    """
    def __init__(self, user_settings=None, defaults=None):
        if user_settings:
            self._user_settings = user_settings
        self.defaults = defaults or DEFAULTS

    @property
    def user_settings(self):
        if not hasattr(self, '_user_settings'):
            self._user_settings = getattr(settings, 'NIGHTMARE_PDF', {})
        return self._user_settings

    def __getattr__(self, attr):
        if attr not in self.defaults:
            raise AttributeError("Invalid Nightmare PDF setting: '%s'" % attr)

        try:
            # Check if present in user settings
            val = self.user_settings[attr]
        except KeyError:
            # Fall back to defaults
            val = self.defaults[attr]

        # Cache the result
        setattr(self, attr, val)
        return val


pdf_settings = PDFSettings(None, DEFAULTS)


def reload_pdf_settings(*args, **kwargs):
    global pdf_settings
    setting, value = kwargs['setting'], kwargs['value']
    if setting == 'NIGHTMARE_PDF':
        pdf_settings = PDFSettings(value, DEFAULTS)


setting_changed.connect(reload_pdf_settings)
