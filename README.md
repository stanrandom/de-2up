# de-2up

I had some documentation as a PDF and it had been formatted for printing. The first page was on a page of its own, and then subsequent pages were formatted side-by-side on pages of the PDF. I know that's a great description by itself, but here's a screenshot.

![screenshot](doc/Screenshot%202026-10-08%20at%2010.38.20.png)

This wouldn't be problematic but I wanted to read this document on my e-reader (which prefers portrait mode) and the text was way too tiny for my old man eyes to be able to read. I needed to separate each doubled page into separate pages.

I get that this is niche but it ticked my box and I'm sharing it just in case anyone else can use it.

It'll create a PDF with `-FORCED-A4` at the end of the filename.

```shell
$ uv run de-2up.py ./a.pdf
reading from ./a.pdf
creating
writing to ./a-FORCED-A4.pdf
$
```

I think the code is fairly readable but the logic is

```
If the current page is wider than it is high (i.e., landscape):
  split it down its midpoint and write both pages to the output file
else
  just pass it through (assuming it's portrait)
```
