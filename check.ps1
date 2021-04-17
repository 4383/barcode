clear
ls

if (pip show barcode-generator) {pip uninstall barcode-generator -y}


python setup.py install

''
''
''
''
''

echo "barcode 1234567890123"
barcode 1234567890123

''
''
''
''
''

echo "barcode 1234567890123 -m -a -v"
barcode 1234567890123 -m -a -v

''
''
''
''
''

echo "barcode 1234567890123 --ascii --html --svg"
barcode 1234567890123 --ascii --html --svg

''
''
''
''
''

echo "barcode 1234567890123 --ascii --html --svg -o 'these fruits, these vegetables'"
barcode 1234567890123 --ascii --html --svg -o 'these fruits, these vegetables'

''
''
''
''
''

pip uninstall barcode-generator -y
rm "these fruits, these vegetables.*"
rm "barcode-1234567890123.*"