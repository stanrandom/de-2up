#!/usr/bin/env python3

import os
import sys

import pypdf

compress = False

if len(sys.argv) < 2:
    print(f'{sys.argv[0]} <filename>')
    sys.exit()

IN_FILE = sys.argv[1]

splitted = os.path.splitext(IN_FILE)
OUT_FILE = splitted[0] + "-FORCED-A4" + splitted[1]
if os.path.exists(OUT_FILE):
    print(f"{OUT_FILE} already exists so be careful.")
    sys.exit()

print(f"reading from {IN_FILE}")
try:
    reader = pypdf.PdfReader(IN_FILE)
except:
    print("file not found or something")
    sys.exit()

print("creating")
writer = pypdf.PdfWriter()
for page in reader.pages:
    box = page.mediabox
    if box.width < box.height:
        writer.add_page(page)
    else:
        left=writer.add_page(page)
        left.cropbox.lower_right=(
            box.right/2,
            box.bottom,
        )
        right=writer.add_page(page)
        right.cropbox.upper_left=(
            box.right/2,
            box.top,
        )

if compress:
    print("compressing")
    for page in writer.pages:
        page.compress_content_streams()

print(f"writing to {OUT_FILE}")
writer.write(OUT_FILE)