# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

"""
Be sure to check the learn guides for more usage information.

This example is for use on (Linux) computers that are using CPython with
Adafruit Blinka to support CircuitPython libraries. CircuitPython does
not support PIL/pillow (python imaging library)!

Author(s): Melissa LeBlanc-Williams for Adafruit Industries
"""

import qwiic_twist
import busio
import digitalio
import board
import time
from gtts import gTTS
import os
from time import strftime, sleep
from PIL import Image, ImageDraw, ImageFont
from audioplayer import AudioPlayer
import adafruit_rgb_display.ili9341 as ili9341
import adafruit_rgb_display.st7789 as st7789  # pylint: disable=unused-import
import adafruit_rgb_display.hx8357 as hx8357  # pylint: disable=unused-import
import adafruit_rgb_display.st7735 as st7735  # pylint: disable=unused-import
import adafruit_rgb_display.ssd1351 as ssd1351  # pylint: disable=unused-import
import adafruit_rgb_display.ssd1331 as ssd1331  # pylint: disable=unused-import

i2c = busio.I2C(board.SCL, board.SDA)


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


# Set up twist
twist = qwiic_twist.QwiicTwist()
twist.begin()
default_blue = 255
default_red = 100
twist.set_blue(default_blue)
twist.set_red(default_red)
twist.set_green(0)

def scale_crop_image(input_image):
    # Scale the image to the smaller screen dimension
    image_ratio = input_image.width / input_image.height
    screen_ratio = width / height
    if screen_ratio < image_ratio:
        scaled_width = input_image.width * height // input_image.height
        scaled_height = height
    else:
        scaled_width = width
        scaled_height = input_image.height * width // input_image.width
    input_image = input_image.resize((scaled_width, scaled_height), Image.BICUBIC)

    # Crop and center the image
    x = scaled_width // 2 - width // 2
    y = scaled_height // 2 - height // 2
    input_image = input_image.crop((x, y, x + width, y + height))

    return input_image


def get_recommendation(mood):
    recommendation = 0
    if mood == "cheerful":
        recommendation = 0
    elif mood == "gloomy":
        recommendation = 1
    elif mood == "anxiety":
        recommendation = 2
    elif mood == "relax":
        recommendation = 3      
    else:
        recommendation = 4
    return recommendation

def say(message):
    audio_filename = "temp.mp3"
    google_tts = gTTS(message, lang = 'en')
    google_tts.save(audio_filename)
    os.system("/usr/bin/mplayer " + audio_filename)

def display_image():
    img_music_player = image
    img_music_player = Image.open("music_player.jpeg")
    img_music_player = scale_crop_image(img_music_player)
    display.image(img_music_player, rotation)

def play(recommendation_num):
    music = ''
    if recommendation_num == 0:
        music = './musics/Updown_Funk.mp3'
    elif recommendation_num == 1:
        music = './musics/Never_Grow_Old.mp3'
    elif recommendation_num == 2:
        music = './musics/Weightless.mp3'
    elif recommendation_num == 3:
        music = './musics/Faded.mp3'
    elif recommendation_num == 4:
        music = './musics/Other.mp3'
    return music

def play_music():
    global music_to_play
    music_to_play.play()

def pause_music():
    global music_to_play, pause
    if pause == 'not_paused':
        music_to_play.pause()
        pause = 'paused'
    else:
        music_to_play.resume()
        pause = 'not_paused'

def stop_music():
    global music_to_play
    music_to_play.close()

def set_volume():
    global music_to_play, current_count, default_red, twist
    current_vol = music_to_play.volume 
    print(current_vol) 
    if twist.get_count() < current_count:
        music_to_play.volume -= 0.25
        default_red -= 1
        twist.set_red(default_red)
        current_count = twist.get_count()
    elif twist.get_count() > current_count:
        music_to_play.volume += 0.25
        default_red += 1
        twist.set_red(default_red)
        current_count = twist.get_count()      

display_image()
say("Hello, welcome back! What is your mood today? Or tell me what happened today? I will play a music based on your mood!")
user_answer = input("Enter your mood: (cheerful, gloomy, anxiety, relax, other)")
music_name = play(get_recommendation(user_answer))
music_to_play = AudioPlayer(music_name)
music_to_play.volume = 50
play_music()
pause = 'not_paused'
keep_listening = True
flag = True
current_count = twist.get_count()
print(current_count)
while keep_listening:
    while flag:
        user_input = input("Enter command: ")
        if user_input == 'p':
            pause_music()
        elif user_input == 's':
            stop_music()
            flag = False
        elif user_input == 'v':
            current_time = time.time()
            while time.time()<current_time + 4:
                set_volume()
                print(twist.get_count())
    say("Would you like to listen to another song?")
    user_choice = input("Enter choice: ")
    if user_choice == "No":
        say("Thank you for using the autonomous music player! Goodbye!")
        keep_listening = False
    elif user_choice == "Yes":
        say("Sounds good! Tell me how you feel right now.")
        flag = True
        user_answer = input("Enter your mood: (cheerful, gloomy, anxiety, relax, other)")
        music_name = play(get_recommendation(user_answer))
        music_to_play = AudioPlayer(music_name)
        music_to_play.volume = 50
        play_music()
        pause = 'not_paused'

   







