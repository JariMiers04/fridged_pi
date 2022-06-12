import os
import math
import time
import signal
from datetime import date
from datetime import datetime
from datetime import timedelta
from rpi_lcd import LCD
from rgb import RGB
from barcode import BARCODE
from scale import SCALE
from food import FOOD
from gpiozero import LightSensor
import RPi.GPIO as GPIO
from os.path import dirname, abspath
from dotenv import load_dotenv

path = dirname(abspath(__file__)) + '/.env'
load_dotenv(path)
 
envUrl = os.getenv('url')

lcd1 = LCD()
barcode = BARCODE()
scale = SCALE()

todayDate = date.today()
expirationDate = todayDate + timedelta(days=5)

parkingSpots = [
    {"checkState": True, "value": LightSensor(4), "led": RGB(27,22,17), "posted": False, "deleted": False},
    {"checkState": True, "value": LightSensor(11), "led": RGB(24,25,23), "posted": False, "deleted": False}
    ]

maxSlotsParking = 2

def PrintProductToLcd(short_name, expiration_date, weight):
    weigthToString =  str(weight)

    lcdString = short_name + "  " + expiration_date + " " + weigthToString + "g"
    lcd1.text(lcdString, 1)

def PrintFullToLcd(full):
    lcd1.clear()
    lcd1.text(full, 1)


def CheckParkingSlots(time):
    endTimer = datetime.now() + timedelta(seconds = time)
    while True:
        start =  datetime.now()
        try:
            if len(parkingSpots) == maxSlotsParking:
                for parking in parkingSpots:
                    print(math.floor(parking.get("value").value * 1000))

                    if math.floor(parking.get("value").value * 1000) < 400:
                        parking["checkState"] = False

                    if math.floor(parking.get("value").value * 1000) > 400:
                        parking.get("led").WhiteFlash()
                        if parking["checkState"] == True:
                            
                            if "product" in parking.keys():
                    
                                if parking["deleted"] == False:
                                    FOOD.DeleteFood(parking["product"])
                                    del parking["product"]
                                    lcd1.clear()
                                    PrintFullToLcd("ONE PLACE OPEN")
                                    parking["deleted"] = True
                                    return
                        parking["checkState"] = True
            if start >= endTimer and parkingSpots[0]["checkState"] == False or parkingSpots[1]["checkState"] == False:
                if parkingSpots[0]["checkState"] == False and parkingSpots[1]["checkState"] == False:
                    lcd1.clear()
                    PrintFullToLcd("NO MORE PLACE IN YOUR FRIDGE")
                    break
                break

        except(KeyboardInterrupt, SystemExit):
            print("crashed")
            GPIO.cleanup()

def FullParking():
        lcd1.clear()
        PrintFullToLcd("NO MORE PLACE IN YOUR FRIDGE")
        CheckParkingSlots(5)
        Init()


def AddProductParkingSlot(food):
    endTimer = datetime.now() + timedelta(seconds = 15)
    while True:
        start =  datetime.now()
        try:
            if start >= endTimer and parkingSpots[0]["checkState"]== True and parkingSpots[1]["checkState"] == True:
                PrintFullToLcd("You didn't fridged...")
                break
            if len(parkingSpots) == maxSlotsParking:
                for parking in parkingSpots:
                    print(math.floor(parking.get("value").value * 1000))

                    if math.floor(parking.get("value").value * 1000) < 400:
                        parking["checkState"] = False

                        if parking["checkState"] == False:
                            parking["product"] = food

                            if parking["posted"] == False:
                                food.PostFood()
                                lcd1.clear()
                                PrintProductToLcd(food.short_name, food.expiration_date, food.weight)
                                parking["posted"] = True
                                return

                    if math.floor(parking.get("value").value * 1000) > 400:
                        parking.get("led").WhiteFlash()
                        if parking["checkState"] == True:
                            
                            if "product" in parking.keys():
                    
                                if parking["deleted"] == False:
                                    FOOD.DeleteFood(food)
                                    del parking["product"]
                                    lcd1.clear()
                                    PrintFullToLcd("ONE PLACE OPEN")
                                    parking["deleted"] = True
                                    return
                        parking["checkState"] = True
            else:
                print("The length of the array is longer than the provided parkings slots")

        except(KeyboardInterrupt, SystemExit):
            print("crashed")
            GPIO.cleanup()

def ScanWeighPost():
    try:
        barcode.ReadBarcode()
        barcodeData = barcode.objectValueData
        print(barcodeData)
        if len(barcodeData) == 0:
            Init()
        else:
            scale.GetWeight()
            scaleWeight = scale.weight
            print(barcodeData, scaleWeight)
            food = FOOD(str(expirationDate),scaleWeight, barcodeData[0].get("short_name"), barcodeData[0].get("long_name"), barcodeData[0].get("nutriscore_label"), barcodeData[0].get("segment_name"), barcodeData[0].get("barcode"), barcodeData[0].get("image"))
            AddProductParkingSlot(food)
    except(KeyboardInterrupt,SystemExit):
        GPIO.cleanup()

def Init():
    while True:
        try:
            if parkingSpots[0]["checkState"] == True or parkingSpots[1]["checkState"] == True:
                
                if parkingSpots[0]["checkState"] == False or parkingSpots[1]["checkState"] == False:
                    print("One Item in fridge")
                    CheckParkingSlots(0)

                    if parkingSpots[0]["checkState"] == False and parkingSpots[1]["checkState"] == False:
                        FullParking()
                ScanWeighPost()

            else: 
                FullParking()
            
        except(KeyboardInterrupt, SystemExit):
            print('Script main.py ended')
            lcd1.clear()
            GPIO.cleanup()


Init()