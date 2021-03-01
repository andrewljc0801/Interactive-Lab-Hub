# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

"""
Be sure to check the learn guides for more usage information.

This example is for use on (Linux) computers that are using CPython with
Adafruit Blinka to support CircuitPython libraries. CircuitPython does
not support PIL/pillow (python imaging library)!

Author(s): Melissa LeBlanc-Williams for Adafruit Industries
"""

import digitalio
import board
from time import strftime, sleep
from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.ili9341 as ili9341
import adafruit_rgb_display.st7789 as st7789  # pylint: disable=unused-import
import adafruit_rgb_display.hx8357 as hx8357  # pylint: disable=unused-import
import adafruit_rgb_display.st7735 as st7735  # pylint: disable=unused-import
import adafruit_rgb_display.ssd1351 as ssd1351  # pylint: disable=unused-import
import adafruit_rgb_display.ssd1331 as ssd1331  # pylint: disable=unused-import

# Configuration for CS and DC pins (these are PiTFT defaults):
cs_pin = digitalio.DigitalInOut(board.CE0)
dc_pin = digitalio.DigitalInOut(board.D25)
reset_pin = digitalio.DigitalInOut(board.D24)

# Config for display baudrate (default max is 24mhz):
BAUDRATE = 24000000

# Setup SPI bus using hardware SPI:
spi = board.SPI()

# pylint: disable=line-too-long
# Create the display:
# disp = st7789.ST7789(spi, rotation=90,                            # 2.0" ST7789
# disp = st7789.ST7789(spi, height=240, y_offset=80, rotation=180,  # 1.3", 1.54" ST7789
# disp = st7789.ST7789(spi, rotation=90, width=135, height=240, x_offset=53, y_offset=40, # 1.14" ST7789
# disp = hx8357.HX8357(spi, rotation=180,                           # 3.5" HX8357
# disp = st7735.ST7735R(spi, rotation=90,                           # 1.8" ST7735R
# disp = st7735.ST7735R(spi, rotation=270, height=128, x_offset=2, y_offset=3,   # 1.44" ST7735R
# disp = st7735.ST7735R(spi, rotation=90, bgr=True,                 # 0.96" MiniTFT ST7735R
# disp = ssd1351.SSD1351(spi, rotation=180,                         # 1.5" SSD1351
# disp = ssd1351.SSD1351(spi, height=96, y_offset=32, rotation=180, # 1.27" SSD1351
# disp = ssd1331.SSD1331(spi, rotation=180,                         # 0.96" SSD1331
display = st7789.ST7789(
    spi,
    cs=cs_pin,
    dc=dc_pin,
    rst=reset_pin,
    baudrate=BAUDRATE,
    width=135,
    height=240,
    x_offset=53,
    y_offset=40,
)
# pylint: enable=line-too-long

# Create blank image for drawing.


height = display.width
width = display.height

image = Image.new("RGB", (width, height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)



# Draw some shapes.
# First define some constants to allow easy resizing of shapes.
rotation = 90
padding = -2
top = padding
bottom = height - padding
# Move left to right keeping track of the current x position for drawing shapes.
x = 0


# Draw a black filled box to clear the image.
draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 0))
display.image(image, rotation)

# Alternatively load a TTF font.  Make sure the .ttf font file is in the
# same directory as the python script!
# Some other nice fonts to try: http://www.dafont.com/bitmap.php
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 24)

# Turn on the backlight
backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True

buttonA = digitalio.DigitalInOut(board.D23)
buttonB = digitalio.DigitalInOut(board.D24)
buttonA.switch_to_input()
buttonB.switch_to_input()

stage = 0

def getSuffix(day):
    suffix = ""
    if (day >= 11 and day <= 13):
        suffix = "th"
    else:
        generate_suffix = {
        1: "st",
        2: "nd",
        3: "rd"
        }
        suffix = generate_suffix.get(day%10, "th")
    return suffix

def get_recommendation(hour):
    recommendation = ""
    if hour < 7 and hour > 0:
        recommendation = "Sleep"
    elif hour >= 7 and hour < 8:
        recommendation = "Have breakfast."
    elif hour >= 8 and hour < 12:
        recommendation = "Study/Work"
    elif hour >= 12 and hour < 13:
        recommendation = "Have lunch."
    elif hour >= 13 and hour < 14:
        recommendation = "Take a nap."
    elif hour >= 14 and hour < 18:
        recommendation = "Study/Work"
    elif hour >= 18 and hour < 19:
        recommendation = "Have dinner."
    elif hour >= 19 and hour < 22:
        recommendation = "Relax!"
    elif hour >= 22 and hour < 24:
        recommendation = "Time to sleep!"
    return recommendation


while True:

    year = strftime("%Y")
    month = strftime("%B")
    day = strftime("%-d")
    day_suffix = getSuffix(int(day))
    weekday = strftime("%A")
    hour = strftime("%H")
    minute = strftime("%M")
    second = strftime("%S")

    date = month + " " + day + day_suffix + ", " + year
    clock = hour + ": " + minute + ": " + second

    if buttonA.value and buttonB.value:
        stage = 0  
    if buttonB.value and not buttonA.value:  # just button A pressed
        stage = 1 # display the clock
    if buttonA.value and not buttonB.value:  # just button B pressed
        stage = 2 # display the recommendation

  
    if stage == 0:
        # Draw a black filled box to clear the image.
        draw.rectangle((0, 0, width, height), outline=0, fill=0)
        y = top+50
        draw.text((x+60, y), "Welcome!", font=font, fill="#FF0000")
        display.image(image, rotation)
    elif stage == 1:
        # Draw a black filled box to clear the image.
        draw.rectangle((0, 0, width, height), outline=0, fill=0)
        # Print out the time
        y = top+30
        draw.text((x+70, y), weekday, font=font, fill="#8000FF")
        y += font.getsize(weekday)[1]
        draw.text((x+20, y), date, font=font, fill="#FF8000")
        y += font.getsize(date)[1]
        draw.text((x+60, y), clock, font=font, fill="#00FF80")
        display.image(image, rotation)
        sleep(0.75)
    elif stage == 2:
        # Draw a black filled box to clear the image.
        draw.rectangle((0, 0, width, height), outline=0, fill=0)
        y = top+50
        activity = get_recommendation(int(hour))
        draw.text((x+90, y), activity, font=font, fill="#8000FF")
        display.image(image, rotation)



