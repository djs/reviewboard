#!/usr/bin/env python
import sys
import os
from pygments.styles import get_all_styles
from pygments.formatters import HtmlFormatter

def main():
    if len(sys.argv) == 2:
        dir = sys.argv[1]
    else:
        dir = '.'

    styles = list(get_all_styles())

    for style in styles:
        fh = open(os.path.join(dir, style + '.css'), 'w')
        fh.write(HtmlFormatter().get_style_defs())
        fh.close()

if __name__ == '__main__':
    main()

