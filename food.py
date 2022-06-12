import os
import requests
from os.path import dirname, abspath
from dotenv import load_dotenv


headers = {"Content-Type": "application/json; charset=utf-8"}

path = dirname(abspath(__file__)) + '/.env'
load_dotenv(path)
 
envUrl = os.getenv('url')

class FOOD(object):

    def __init__(self, expiration_date, weight, short_name, long_name, nutriscore_label, segment_name, barcode, image):
        self.expiration_date = expiration_date
        self.weight = weight
        self.short_name = short_name
        self.long_name = long_name
        self.nutriscore_label = nutriscore_label
        self.segment_name = segment_name
        self.barcode = barcode
        self.image = image

    def PostFood(food):
        postUrl = envUrl + "/food"

        data = {
            'expiration_date': food.expiration_date,
            'weight': food.weight,
            'short_name': food.short_name,
            'long_name': food.long_name,
            'segment_name': food.segment_name,
            'barcode': food.barcode,
            'image': food.image
        }
        print(data)

        sendPost = requests.post(postUrl, headers=headers, json=data)

        return sendPost
    def DeleteFood(food):
        deleteUrl = envUrl + "/food/" + food.barcode


        deletePost = requests.delete(deleteUrl)

        return deletePost