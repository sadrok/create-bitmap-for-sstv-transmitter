# create-bitmap-for-sstv-transmitter

Simple script that creates a bitmap from the lines of text using the 
provided font-table. It should be fairly "configurable" but the defaults are:
* 8x11 pixel fonts
* All caps letters, digits, and some symbols

The purpose of the script is to provide the C hex values to plug into
a Arduino sketch that transmits the bitmap and potentially any other
dynamic text using SSTV.

## Usage
1. run `pipenv shell` to setup the virtual environment. It should install
the packages as specified in the `Pipfile.lock` file.

2. run `python main.py` - it will generate the text in the script and
output a string that can be copy & pasted into the Arduino sketch.
It should also display the bitmap using whichever application is associated
with images.

## TODO
* Read the text from `stdin` instead of just the coded lines of text
inside the script.

  