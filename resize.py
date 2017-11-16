#!/usr/bin/python
from __future__ import division
import pygame
import sys

# height is determined by template used for PDF generation
MAX_WIDTH = 550
MAX_HEIGHT = 730

def w_larger(width, height):
    DECREASE = width - MAX_WIDTH
    RATIO = round(DECREASE / width, 2)
    scaled_width = width * (1 - RATIO)
    scaled_height = height * (1 - RATIO) 
    return scaled_width, scaled_height

def h_larger(width, height):
    DECREASE = height - MAX_HEIGHT
    RATIO = round(DECREASE / height, 2)
    scaled_width = width * (1 - RATIO)
    scaled_height = height * (1 - RATIO) 
    return scaled_width, scaled_height

def both_larger(width, height):
    if width > height:
        # width is largest value
        DECREASE = width - MAX_WIDTH
        RATIO = round(DECREASE / width, 2)
        scaled_width = width * (1 - RATIO)
        scaled_height = height * (1 - RATIO) 
    if height > width:
        # height is the largest
        DECREASE = height - MAX_HEIGHT
        RATIO = round(DECREASE / height, 2)
        scaled_width = width * (1 - RATIO)
        scaled_height = height * (1 - RATIO) 
    return scaled_width, scaled_height

def smart_resize(width,height):
    if width > MAX_WIDTH and height > MAX_HEIGHT:
        return both_larger(width,height)
    elif width > MAX_WIDTH:
        return w_larger(width,height)
    elif height > MAX_HEIGHT:
        return h_larger(width,height)
    else:
        return width, height
