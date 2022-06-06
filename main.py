import time
import sys
import math
import os
from turtle import dot
from rpi_lcd import LCD
import json
from rgb import RGB
from barcode import BARCODE
from scale import SCALE
import requests
from gpiozero import LightSensor
import RPi.GPIO as GPIO
from os.path import dirname, abspath
from dotenv import load_dotenv

headers = {"Content-Type": "application/json; charset=utf-8"}

testData = {
    "expiration_date": "2022-06-08",
    "weight": 250,
    "short_name":"zwan",
	"long_name":"zwan",
	"segment_name":"Worsten Conserv",
	"nutriscore_label":"D",
	"barcode":"00000025190359",
	"image":"https:\/\/static.colruyt.be\/images\/200x310\/std.lang.all\/31\/28\/asset-1463128.jpg"
}

# sendPost = requests.post(url, headers=headers, json=testData)

path = dirname(abspath(__file__)) + '/.env'
load_dotenv(path)
 
envUrl = os.getenv('url')

print(envUrl)
print(requests.get(envUrl).content)

lcd1 = LCD()
barcode = BARCODE()
barcodeData = barcode.objectValueData
scale = SCALE()

rgb1 = RGB(27,22,17)
rgb2 = RGB(24,25,23)
ldr1 = LightSensor(4)
ldr2 = LightSensor(11)


def PrintToLcd(weight):
    value =  str(weight)
    lcd1.text(value + ' g', 1)



def TestParking():
    print('code continues')

def Init():
    try:
        print("init function")
        barcode.ReadBarcode()
        scale.GetWeight()
        scaleWeight = scale.weight
        print(barcodeData, scaleWeight)
        PrintToLcd(scaleWeight)
    except(KeyboardInterrupt, SystemExit):
        print('Script main.py ended')
        GPIO.cleanup()
Init()


# while True:
#     try:
#         weightValue = math.floor(scale.get_weight(5))
#         rgb1.RedFlash()
#         print("eerste ldr" , ldr1.value * 100)
#         print("tweede ldr" , ldr2.value * 100)
#         if weightValue < 0:
#             weightValue = 0
#             print(weightValue)
#         if weightValue > 0:
#             scaleArray.append(weightValue)
#             if len(scaleArray) > 3:
#                 if scaleArray[-2] == scaleArray[-1]:
#                     rgb1.GreenFlash()
#                     GetWeightScale(scaleArray[-1])

#     except(KeyboardInterrupt, SystemExit):
#         CleanAndExitScale()
