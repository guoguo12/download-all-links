#!/usr/bin/env python

"""download.py: Downloads all links on the given HTML page."""

__author__  = "Allen Guo"
__license__ = "GNU GPLv3"
__version__ = "1.0"

import collections
import os
import re
import time
import urllib2

PATTERN = re.compile('.*<a.*href="(.*)">', re.DOTALL)

def getExtension(name):
    return name.split('.')[-1]

def getFullURL(url, baseUrl):
    fullURL = url
    if not url.startswith(('http://', 'https://')):
        fullURL = baseUrl.rstrip('/') + '/' + url.lstrip('/')
    return fullURL

def getName(url):
    return urllib2.unquote(url).split('/')[-1]

def read(name):
    file = open(name, 'r')
    data = file.read()
    file.close()
    return data

def download(url, name):
    data = urllib2.urlopen(url).read()
    size = len(data)
    file = open(name, 'wb')
    file.write(data)
    file.close()
    return size

def printPrologue():
    os.system('cls')
    print '*' + '-' * 22 + '*'
    print '| Download All Links   |'
    print '| Created by Allen Guo |'
    print '*' + '-' * 22 + '*\n'

def printLinks(links):
    print '=== Links Found ==='
    print len(links), 'links found'
    print '-' * 19
    for title in links:
        print 'URL:', links[title]
        print 'Title:', title
        print '-' * 19

def printDownloadReport(downloadData):
    size = downloadData[0]
    elapsed = downloadData[1]
    print '\n=== Download Report ==='
    print 'Total download size (KiB):', size / 1024.0
    if elapsed != 0:
        print 'Time elapsed (s):', elapsed
        print 'Download rate (Mb/s):', 8e-6 * size / elapsed

def extract(extensions, sourceFile):
    start = 0
    links = collections.OrderedDict()
    if sourceFile.startswith(('http://', 'https://')):
        source = urllib2.urlopen(sourceFile).read()
    else:
        source = read(sourceFile)
    while source.find('</a>', start) != -1:
        end = source.find('</a>', start) + 4
        scanText = source[start:end]
        match = PATTERN.match(scanText)
        if match != None:
            url = match.group(1)
            if getExtension(url) in extensions:
                links[getName(url)] = url
        start = end
    return links

def downloadLinks(links, baseUrl, outputDirectory):
    size = 0
    raw_input('Press ENTER to begin downloading\n')
    print '=== Now Downloading ==='
    if not os.path.exists(outputDirectory):
        os.makedirs(outputDirectory)
        print 'Output directory', outputDirectory, 'created'
    else:
        print 'Output directory', outputDirectory, 'exists'
    start = time.time()
    for title in links.keys():
        url = getFullURL(links[title], baseUrl)
        print 'Downloading', title + '...'
        size += download(url, outputDirectory + title)
    elapsed = time.time() - start
    print 'Downloads complete'
    return (size, elapsed)

def downloadAllLinks(baseUrl, extensions, outputDirectory, sourceFile):
    printPrologue()
    links = extract(extensions, sourceFile)
    printLinks(links)
    downloadData = downloadLinks(links, baseUrl, outputDirectory)
    printDownloadReport(downloadData)

if __name__ == '__main__':
    printPrologue()
    print 'Download All Links cannot be run directly from the command line.'
    print 'See the online documentation for Download All Links for details.'