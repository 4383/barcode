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

`$ barcode 0123456789123`

`$ barcode 0123456789123 --ascii --html --svg`

`$ barcode 0123456789123 --ascii --html --svg -o ["these fruits, these vegetables"](https://www.youtube.com/watch?v=lHU_AJfrZlM)` 

`$ python barcode.py`

Options
-------
* `-m | --motif` Display motif
* `-o | --outfile` Output filename. Save SVG/ASCII/HTML output(s) into a file with this filename. Extensions will be set automatically. Defaults to argument
* `-c | --copy` Copy to clipboard
* `-a | --author` Display software information
* `-v | --version` Display version'
* `--ascii` Display the ASCII value on the standard output
* `--svg` Display the svg value on the standard output
* `--html` Display the svg value on the standard output




About
-----
Written by Hervé BERAUD
Retrieve on Pypi => https://pypi.python.org/pypi/barcode-generator/

https://www.youtube.com/watch?v=lHU_AJfrZlM