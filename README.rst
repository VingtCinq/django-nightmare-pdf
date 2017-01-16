|nightmare-pdf v0.0.1 on PyPi| |MIT license| |Stable|

django-nightmare-pdf
====================

Convert HTML to pdf with django using nightmare

Requirements
------------

-  Python (2.7) (Need to be tested for 3.x)
-  Django (1.10) (Need to be tested for previous versions)

Dependencies
------------

This django app depends on
`Nightmare <https://github.com/segmentio/nightmare>`__, you need to
first install it using ``npm``:

``npm install nightmare``

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

Usage
-----

Generate a pdf from an url and save it to database, or retrieve it as a
ContentFile, or return it inside an HttpResponse :

::

    from nightmare_pdf import PDFGenerator

    pdf = PDFGenerator(url="https://github.com/charlesthk/django-nightmare-pdf",

    # Save it to database and retrieve a PdfDoc Object (database):
    pdf.save(
            filename='nightmare_pdf',
            title="nightmare_pdf on github",
            description="Convert HTML to pdf with django using nightmare")

    # Get the PDf as a Django ContentFiel :
    pdf_content_file = pdf.get_content_file('nightmare_pdf') 

    # Return a Django HttpResponse with the PDF Attached :
    return pdf.get_http_response('nightmare_pdf')

Support
-------

If you are having issues, please let us know or submit a pull request.

License
-------

The project is licensed under the MIT License.

.. |nightmare-pdf v0.0.1 on PyPi| image:: https://img.shields.io/badge/pypi-0.0.1-green.svg
   :target: https://pypi.python.org/pypi/nightmare-pdf
.. |MIT license| image:: https://img.shields.io/badge/licence-MIT-blue.svg
.. |Stable| image:: https://img.shields.io/badge/status-stable-green.svg

