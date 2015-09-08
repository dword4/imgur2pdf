#### Requires
* reportlab
* imgurpython
* PIL

#### Description
Pulls down the contents of an Imgur album and creates a PDF file complete with titles and descriptions for each of the images.

#### Setup
Add your imgur API credentials to credentials.py then rename it to creds.py

#### Notes
Written to work with Python 2.7.5, if you get messages when running it about InsecurePlatformWarning you need to install libffi-dev then run pip install requests[security] to resolve the issue.
