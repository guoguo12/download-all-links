Download All Links
==================

Download All Links allows you to download all files linked from a given webpage with Python. 
It also has a basic download report feature.

Documentation
-------------

You will need Python to use Download All Links. Python 2.7 is preferred.

### download.py

The `download.py` file handles the entire process. You need to provide four variables to proceed:
* `baseUrl` is the URL of the parent directory from which files are downloaded
(assuming the file paths are provided relative to the parent directory).
* `extensions` is a list of strings that describe the types of files to download.
Do not include periods (e.g., for text files, use "txt" not ".txt").
* `outputDirectory` is the directory to which the files will be downloaded. 
The string should end with two backslashes. If the directory does not exist, it will be created.
* `source` is the local file or webpage containing the HTML source from which links are scraped.

Note that all files should be relative or absolute and all URLs should begin with "http://" (or "https://").

To begin the download process, call `downloadAllLinks()` with the arguments from above (in that order)
and follow the on-screen instructions where necessary.

### example.py

The `example.py` file contains an example of Download All Links in use. 
The example downloads all files ending in ".htm", ".txt", or ".mp3" linked from [this site](http://www.iana.org/domains/special.html).

Errors
------

Download All Links currently does not attempt to handle any errors.
If you encounter an error you cannot resolve, please use the GitHub Issues feature to report the bug. Thanks!

License
-------

Download All Links is licensed under the [GNU GPLv3](http://www.gnu.org/licenses/gpl.html).
