#!/usr/bin/env python

import os
import re
import sys

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
        css = HtmlFormatter(style=style).get_style_defs('.syntax')
        for line in css.split('\n'):
            # remove overall text color style
            line = re.sub('(\.syntax\s+{.*)(color: [^\s]+)\s*(})', '\g<1>\g<3>', line)
            print line
            fh.write(line + '\n')
        fh.close()

if __name__ == '__main__':
    main()

