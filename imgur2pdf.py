#!/usr/bin/python
from imgurpython import ImgurClient
from PIL import Image
from creds import * 
import PIL
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Paragraph, Image, Spacer, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_JUSTIFY
import requests
import progressbar as pb
import shutil
import os
import argparse
import sys
import resize

if sys.version_info[0]== 2:
    pass 
elif sys.version_info[0] == 3:
    from builtins import input

# trying to fix the error messages
import urllib3
urllib3.disable_warnings()

parser = argparse.ArgumentParser(description='imgur2pdf - convert an imgur gallery to pdf for archival purposes')
parser.add_argument('album', metavar='album',  help='id of imgur album')
parser.add_argument('destination', metavar='destination', help='location to save to')
args = parser.parse_args()

client = ImgurClient(client_id, client_secret)
album_data = client.get_album(args.album)
album_file = album_data.title.replace(' ','_')+".pdf"

path = args.destination[:-1] + '/' + album_file

if os.path.isfile(path) == True:
    # we found something!
    print("found file %s, try with another destination" % path)
    quit()
else:
    # nothing found, lets make stuff
    pass


doc = SimpleDocTemplate(path,pagesize=letter,
                        rightMargin=25,leftMargin=25,
                        topMargin=25,bottomMargin=25)
ParagraphStyle(name = 'Normal',
               fontName = "Verdana",
               fontSize = 11,
               leading = 15,
               alignment = TA_JUSTIFY,
               allowOrphans = 0,
               spaceBefore = 20,
               spaceAfter = 20,
               wordWrap = 1)
Story=[]
styles=getSampleStyleSheet()

items = client.get_album_images(str(args.album))
p = 0 
for item in items:
    p += 1
bar = pb.ProgressBar(maxval=p).start()
p = 1
for item in items:

    response = requests.get(item.link, stream=True)
    name = str(item.id)+".jpg"
    with open(name, 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
    del response
    sc = PIL.Image.open(name)
    width, height = sc.size

    # time to look at the size and apply a resize ratio
    """
    if height <= 600 and width <= 800:
        resize_ratio = 0.50
    else :
        resize_ratio = 0.85
    """
    (scaled_width, scaled_height) = resize.smart_resize(width, height)
    #scaled_width = width * resize_ratio
    #scaled_height = height * resize_ratio 

    im = Image(name, scaled_width, scaled_height)
    title = str(item.title)
    if item.title:
        Story.append(Paragraph(item.title, styles["Normal"]))
    Story.append(im)
    if item.description:
        Story.append(Paragraph(item.description, styles["Normal"]))
    Story.append(PageBreak())
    bar.update(p)
    p += 1
doc.build(Story)
print("\nfile created -> "+str(path))
#os.system("rm *.jpg")
# line above commented out for testing purposes
