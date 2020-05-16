import os
import sys

import click
from PIL import Image

FONT8x11 = {
    " ": (0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,),
    "!": (0x00, 0x18, 0x18, 0x18, 0x18, 0x10, 0x10, 0x00, 0x18, 0x18, 0x00,),
    '"': (0x00, 0x3C, 0x46, 0x06, 0x06, 0x0C, 0x10, 0x00, 0x30, 0x30, 0x00,),
    "#": (0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,),
    "$": (0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,),
    "%": (0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,),
    "&": (0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,),
    "'": (0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,),
    "(": (0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,),
    ")": (0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,),
    "*": (0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,),
    "+": (0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,),
    ",": (0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,),
    "-": (0x00, 0x00, 0x00, 0x00, 0x00, 0x7E, 0x7E, 0x00, 0x00, 0x00, 0x00,),
    ".": (0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x06, 0x06, 0x00,),
    "/": (0x00, 0x00, 0x02, 0x06, 0x0E, 0x1C, 0x38, 0x70, 0x60, 0x40, 0x00,),
    "0": (0x00, 0x3C, 0x62, 0x62, 0x66, 0x6A, 0x72, 0x62, 0x62, 0x3C, 0x00,),
    "1": (0x00, 0x38, 0x18, 0x18, 0x18, 0x18, 0x18, 0x18, 0x18, 0x18, 0x00,),
    "2": (0x00, 0x3C, 0x46, 0x06, 0x06, 0x1C, 0x20, 0x60, 0x60, 0x7E, 0x00,),
    "3": (0x00, 0x3C, 0x46, 0x06, 0x06, 0x1C, 0x06, 0x06, 0x46, 0x3C, 0x00,),
    "4": (0x00, 0x0C, 0x1C, 0x2C, 0x4C, 0x4C, 0x7E, 0x0C, 0x0C, 0x0C, 0x00,),
    "5": (0x00, 0x7E, 0x60, 0x60, 0x60, 0x7C, 0x06, 0x06, 0x46, 0x3C, 0x00,),
    "6": (0x00, 0x3C, 0x62, 0x60, 0x60, 0x7C, 0x62, 0x62, 0x62, 0x3C, 0x00,),
    "7": (0x00, 0x7E, 0x06, 0x0C, 0x18, 0x30, 0x30, 0x30, 0x30, 0x30, 0x00,),
    "8": (0x00, 0x3C, 0x62, 0x62, 0x62, 0x3C, 0x62, 0x62, 0x62, 0x3C, 0x00,),
    "9": (0x00, 0x3C, 0x46, 0x46, 0x46, 0x3E, 0x06, 0x06, 0x46, 0x3C, 0x00,),
    ":": (0x00, 0x00, 0x00, 0x18, 0x18, 0x00, 0x00, 0x18, 0x18, 0x00, 0x00,),
    ";": (0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,),
    "<": (0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,),
    "=": (0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,),
    ">": (0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,),
    "?": (0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,),
    "@": (0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,),
    "A": (0x00, 0x18, 0x24, 0x62, 0x62, 0x62, 0x7E, 0x62, 0x62, 0x62, 0x00,),
    "B": (0x00, 0x7C, 0x32, 0x32, 0x32, 0x3C, 0x32, 0x32, 0x32, 0x7C, 0x00,),
    "C": (0x00, 0x3C, 0x62, 0x62, 0x60, 0x60, 0x60, 0x62, 0x62, 0x3C, 0x00,),
    "D": (0x00, 0x7C, 0x32, 0x32, 0x32, 0x32, 0x32, 0x32, 0x32, 0x7C, 0x00,),
    "E": (0x00, 0x7E, 0x60, 0x60, 0x60, 0x7C, 0x60, 0x60, 0x60, 0x7E, 0x00,),
    "F": (0x00, 0x7E, 0x60, 0x60, 0x60, 0x7C, 0x60, 0x60, 0x60, 0x60, 0x00,),
    "G": (0x00, 0x3C, 0x62, 0x62, 0x60, 0x60, 0x66, 0x62, 0x62, 0x3C, 0x00,),
    "H": (0x00, 0x62, 0x62, 0x62, 0x62, 0x7E, 0x62, 0x62, 0x62, 0x62, 0x00,),
    "I": (0x00, 0x3C, 0x18, 0x18, 0x18, 0x18, 0x18, 0x18, 0x18, 0x3C, 0x00,),
    "J": (0x00, 0x1E, 0x0C, 0x0C, 0x0C, 0x0C, 0x4C, 0x4C, 0x4C, 0x38, 0x00,),
    "K": (0x00, 0x62, 0x64, 0x68, 0x70, 0x68, 0x64, 0x62, 0x62, 0x62, 0x00,),
    "L": (0x00, 0x60, 0x60, 0x60, 0x60, 0x60, 0x60, 0x60, 0x60, 0x7E, 0x00,),
    "M": (0x00, 0x42, 0x62, 0x76, 0x6A, 0x62, 0x62, 0x62, 0x62, 0x62, 0x00,),
    "N": (0x00, 0x42, 0x62, 0x72, 0x6A, 0x66, 0x62, 0x62, 0x62, 0x62, 0x00,),
    "O": (0x00, 0x3C, 0x62, 0x62, 0x62, 0x62, 0x62, 0x62, 0x62, 0x3C, 0x00,),
    "P": (0x00, 0x7C, 0x62, 0x62, 0x62, 0x7C, 0x60, 0x60, 0x60, 0x60, 0x00,),
    "Q": (0x00, 0x3C, 0x62, 0x62, 0x62, 0x62, 0x62, 0x6A, 0x6A, 0x3C, 0x08,),
    "R": (0x00, 0x7C, 0x62, 0x62, 0x62, 0x7C, 0x68, 0x64, 0x62, 0x62, 0x00,),
    "S": (0x00, 0x3C, 0x62, 0x60, 0x60, 0x3C, 0x06, 0x06, 0x46, 0x3C, 0x00,),
    "T": (0x00, 0x7E, 0x18, 0x18, 0x18, 0x18, 0x18, 0x18, 0x18, 0x18, 0x00,),
    "U": (0x00, 0x62, 0x62, 0x62, 0x62, 0x62, 0x62, 0x62, 0x62, 0x3C, 0x00,),
    "V": (0x00, 0x62, 0x62, 0x62, 0x62, 0x62, 0x62, 0x22, 0x14, 0x08, 0x00,),
    "W": (0x00, 0x62, 0x62, 0x62, 0x62, 0x62, 0x6A, 0x76, 0x62, 0x42, 0x00,),
    "X": (0x00, 0x42, 0x62, 0x74, 0x38, 0x1C, 0x2E, 0x46, 0x42, 0x42, 0x00,),
    "Y": (0x00, 0x42, 0x62, 0x74, 0x38, 0x18, 0x18, 0x18, 0x18, 0x18, 0x00,),
    "Z": (0x00, 0x7E, 0x06, 0x0E, 0x0C, 0x18, 0x30, 0x70, 0x60, 0x7E, 0x00,),
}

CHARACTER_WIDTH = 8
CHARACTER_HEIGHT = 11


@click.command("main")
@click.argument("filename", required=False)
@click.option("--center-align", type=click.BOOL, default=False, is_flag=True)
def run(filename=None, center_align=False):

    if filename:
        print(f"Reading lines from file: {filename}")
        lines = open(filename, "r").readlines()
        print(lines)
    else:
        print(
            "Enter the lines below and terminate with end-of-file character on it's own line"
            " (e.g. Ctrl-Z in Windows or Ctrl-D on linux"
        )
        lines = sys.stdin.readlines()

    line_count = len(lines)
    print(f"Generating bitmap for {line_count} lines")

    lines = [l.strip() for l in lines]
    max_line_length = max(len(line) for line in lines)
    bitmap_width = CHARACTER_WIDTH * max_line_length
    bitmap_height = CHARACTER_HEIGHT * line_count

    lines = [l.upper() for l in lines]
    if center_align:
        lines = [l.center(max_line_length) for l in lines]

    bytemap = [
        0x00
        for _ in range(line_count * CHARACTER_HEIGHT)
        for _ in range(max_line_length)
    ]

    for line, line_text in enumerate(lines):
        for y in range(CHARACTER_HEIGHT):
            for c, char in enumerate(line_text):
                pos = line * max_line_length * CHARACTER_HEIGHT
                pos += y * max_line_length
                pos += c
                bytemap[pos] = FONT8x11.get(char, (0xFF,) * CHARACTER_HEIGHT)[y]

    # Here we print out the "C" style code to be copied into the Arduino code
    print(", ".join("0x{:02x}".format(b) for b in bytemap))

    # This bit just displays the image to see if it looks right as a bitmap
    image = Image.new("1", (bitmap_width, bitmap_height))
    image.putdata([(x & (0x80 >> b)) for x in bytemap for b in range(8)])
    image.show("The Image")


if __name__ == "__main__":
    run()
