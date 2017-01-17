|nightmare-pdf v0.1.10 on PyPi| |MIT license| |Stable|

django-nightmare-pdf
====================

Convert HTML to pdf with django using nightmare

Requirements
------------

-  Python (2.7) (Need to be tested for 3.x)
-  Django (1.10, 1.9) (Need to be tested for previous versions)

Dependencies
------------

This django app depends on
`Nightmare <https://github.com/segmentio/nightmare>`__, you need to
first install it using ``npm``:

``npm install nightmare``

*Warning*, as of today, getting nightmare/electron to work on linux is
not that easy.

Installation
------------

Install using ``pip`` :

``pip install nightmare_pdf``

Add ``nightmare_pdf`` to your INSTALLED\_APPS setting.

::

    INSTALLED_APPS = (
        ...
        'nightmare_pdf',
    )

create a directory to hold pdf files created by Nightmare, default to
``pdf_temp`` :

``mkdir pdf_temp``

Example
-------

Generate a pdf from an url and save it to database, or retrieve it as a
ContentFile, or return it inside an HttpResponse :

::

    from nightmare_pdf.generators import PDFGenerator

    pdf = PDFGenerator(url="https://github.com/charlesthk/django-nightmare-pdf",

    # Save it to database and retrieve a PdfDoc Object (database):
    pdf.save(
            filename='nightmare_pdf',
            title="nightmare_pdf on github",
            description="Convert HTML to pdf with django using nightmare")

    # Get the PDf as a Django ContentFile named 'my_pdf_file.pdf' :
    pdf_content_file = pdf.get_content_file('my_pdf_file') 

    # Return a Django HttpResponse with the PDF Attached named 'my_pdf_file.pdf':
    return pdf.get_http_response('my_pdf_file')

``PDFGenerator`` options
------------------------

The ``PDFGenerator`` class accepts the following arguments :

-  url [required]
-  timeout [Optional] default to 1000, defines the timeout between the
   opening and the rendering of the url by nightmare
-  page\_size [Optional] default to 'A4', accepts options are A3, A4,
   A5, Legal, Letter or Tabloid
-  landscape [Optional] default to 0, defines whether rendering pdf in
   landscape mode
-  print\_background [Optional] default to 1, defines whether printing
   background
-  margins\_type [Optional] default to 1, defines which margins to use.
   Uses 0 for default margin, 1 for no margin, and 2 for minimum margin.
-  script [Optional] default to DEFAULT\_RENDER\_SCRIPT, defines which
   render script to use.
-  temp\_dir [Optional] default to DEFAULT\_TEMP\_DIR, defines which
   temp dir to use.

Model use for saving PDF
------------------------

When using ``save(filename, title='', description='')`` method of
``PDFGenerator``, the following model is used:

::

    class PdfDoc(models.Model):
        """
        Store each generated pdf
        """
        title = models.CharField(verbose_name=_("Title"), max_length=255, blank=True)
        description = models.TextField(verbose_name=_("Description"), blank=True)
        document = models.FileField(verbose_name=_("Document PDF"), upload_to=pdf_settings.UPLOAD_TO)
        created_at = models.DateTimeField(auto_now=False, auto_now_add=True, verbose_name=_('Creation'))
        updated_at = models.DateTimeField(auto_now=True, auto_now_add=False, verbose_name=_('Update'))

Settings
--------

Add your settings to your main django settings file. The settings are
set by default to :

::

    NIGHTMARE_PDF = {
        'UPLOAD_TO': 'pdfs',
        'NODE_PATH': 'node',
        'DEFAULT_RENDER_SCRIPT': os.path.join(NIGHTMARE_PDF_DIR, 'render_pdf.js'),
        'DEFAULT_TEMP_DIR': os.path.join(settings.BASE_DIR, 'pdf_temp')
    }

``UPLOAD_TO``
~~~~~~~~~~~~~

Define the directory or the function to be used when saving PDFs,
default to ``pdfs``.

``NODE_PATH``
~~~~~~~~~~~~~

Define the path to Node binary, default to ``node``.

``DEFAULT_RENDER_SCRIPT``
~~~~~~~~~~~~~~~~~~~~~~~~~

Define which render\_script to use by default, default to
``render_pdf.js`` inside the package.

``DEFAULT_TEMP_DIR``
~~~~~~~~~~~~~~~~~~~~

Define the directory to use for temporarily generated pdf by Nightmare.
default to ``pdf_temp``.

Support
-------

If you are having issues, please let us know or submit a pull request.

License
-------

The project is licensed under the MIT License.

.. |nightmare-pdf v0.1.10 on PyPi| image:: https://img.shields.io/badge/pypi-0.1.10-green.svg
   :target: https://pypi.python.org/pypi/nightmare-pdf
.. |MIT license| image:: https://img.shields.io/badge/licence-MIT-blue.svg
.. |Stable| image:: https://img.shields.io/badge/status-stable-green.svg

