#!/usr/bin/python
from imgurpython import ImgurClient
from PIL import Image
import PIL
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Paragraph, Image, Spacer, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_JUSTIFY
import requests
import shutil
import os

album = raw_input('Album ID:')
client_id = 'get_your_own'
client_secret = 'get_your_own'
client = ImgurClient(client_id, client_secret)
album_file = str(album)+".pdf"
doc = SimpleDocTemplate(album_file,pagesize=letter,
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
items = client.get_album_images(str(album))
for item in items:

        #print(str(item.title))
        response = requests.get(item.link, stream=True)
        name = str(item.id)+".jpg"
        with open(name, 'wb') as out_file:
                shutil.copyfileobj(response.raw, out_file)
        del response
        sc = PIL.Image.open(name)
        width, height = sc.size
        scaled_width = width * 0.15
        scaled_height = height * 0.15

        im = Image(name, scaled_width, scaled_height)
        title = str(item.title)
        if item.title:
                Story.append(Paragraph(item.title, styles["Normal"]))
        Story.append(im)
        if item.description:
                Story.append(Paragraph(item.description, styles["Normal"]))
        Story.append(PageBreak())

doc.build(Story)
print("file created -> "+str(album_file))
os.system("rm *.jpg")