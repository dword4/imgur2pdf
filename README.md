#### Requires
* reportlab
* imgurpython
* PIL (or Pillow if running with Python 3)
* progressbar

#### Description
Pulls down the contents of an Imgur album and creates a PDF file complete with titles and descriptions for each of the images. Filenames are based on the album title and it wont overwrite an existing file.

#### Setup
Add your imgur API credentials to credentials.py then rename it to creds.py

#### Usage
python imgur2pdf.py [albumID] [destination]

#### Notes
If you get messages when running it about InsecurePlatformWarning you need to install libffi-dev then run pip install requests[security] to resolve the issue.

#### Future Plans
more pictures per page, a progress bar, and various other formats as time permits
