# barcode-generator (EAN13 compatible)
Simple lightweight python barcode EAN 13 generator. Output format SVG and ASCII

Only provide EAN 13 barcode type

Summary
-------
* Enter your 13 digits
* Press enter
* Copy output SVG on html file
* Open this html file with browser
* Have Fun !

Install
-------
`$ pip install barcode-generator`

or

`$ git clone http://github.com/4383/barcode`

`$ cd barcode`

`$ python setup.py install`


Usage examples
------
`$ barcode`

`$ barcode -i 0123456789123`

`$ barcode -i 0123456789123 -o my_barcode.html` 

`$ python barcode.py`

Options
-------
* `-i` User input (digits list, len 13 digits strict)
* `-o` Save output into the output filename specified here
* `-ascii` Display barcode ASCII value on the standard output
* `-version` Display version
* `-nb` Hide software informations (No Brand)
* `-h` Show help message

About
-----
Written by Hervé BERAUD
Retrieve on Pypi => https://pypi.python.org/pypi/barcode-generator/0.1rc1
