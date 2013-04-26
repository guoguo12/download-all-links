#!/usr/bin/env python

"""example.py: Demonstrates how to properly use download.py."""

__author__  = "Allen Guo"
__license__ = "GNU GPLv3"
__version__ = "1.0"

import download

def main():
    baseUrl = 'http://www.iana.org/domains/special/'
    extensions = ['htm', 'txt', 'mp3']
    output = 'C:\\Users\\Allen\\Downloads\\'
    source = 'http://www.iana.org/domains/special.html'
    download.downloadAllLinks(baseUrl, extensions, output, source)

if __name__ == '__main__':
    main()