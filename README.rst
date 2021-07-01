barcode-generator (EAN13 compatible)
====================================

.. raw:: html

   <html>

.. raw:: html

   <body>

.. raw:: html

   <center>

.. container::

   .. raw:: html

      <svg>

   0123456789123

   .. raw:: html

      </svg>

.. raw:: html

   </center>

.. raw:: html

   </body>

.. raw:: html

   </html>

| Simple lightweight python barcode EAN 13 generator. Output format SVG
  and ASCII
| Only provide EAN 13 barcode type

Summary
-------

-  Enter your 13 digits
-  Press enter
-  Copy (or save) output in SVG, HTML, or plain text, formats
-  Open this html file with browser
-  Have Fun !

Install
-------

.. code:: shell

   pip install barcode-generator

or

.. code:: shell

   git clone http://github.com/4383/barcode
   cd barcode
   python setup.py install

Usage examples
--------------

``$ barcode``

``$ barcode 0123456789123``

``$ barcode 0123456789123 --ascii --html --svg``

``$ barcode 0123456789123 --ascii --html --svg -o "file_name_without_extension"``

``$ python barcode.py``

Options
-------

.. code:: shell

   -m | --motif
   -o | --outfile
   -c | --copy
   -a | --author
   -v | --version
   --ascii
   --svg
   --html

About
-----

| Written by Hervé BERAUD
| Retrieve on Pypi => https://pypi.python.org/pypi/barcode-generator/
