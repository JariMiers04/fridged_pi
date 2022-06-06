import requests

url = 'http://192.168.0.116:80/food'
headers = {"Content-Type": "application/json; charset=utf-8"}

testData = {
    "expiration_date": "2022-06-08",
    "weight": 250,
    "short_name":"ZW COCKT WORSTJES 210G",
	"long_name":"ZWAN coctailworstjes 210g",
	"segment_name":"Worsten Conserv",
	"nutriscore_label":"D",
	"barcode":"00000025190359",
	"image":"https:\/\/static.colruyt.be\/images\/200x310\/std.lang.all\/31\/28\/asset-1463128.jpg"
}

sendPost = requests.post(url, headers=headers, json=testData)

class FOOD(object):
    expiration_date = ""
    weight = 0
    short_name = ""
    long_name=""
    nutriscore_label=""
    segment_name=""
    barcode=""
    image=""

    def __init__(self, expiration_date, weight, short_name, long_name, nutriscore_label, segment_name, barcode, image):
        self.expiration_date = expiration_date
        self.weight = weight
        self.short_name = short_name
        self.long_name = long_name
        self.nutriscore_label = nutriscore_label
        self.segment_name = segment_name
        self.barcode = barcode
        self.image = image
        print(self)

    def make_food(expiration_date, weight, short_name, long_name, nutriscore_label, segment_name, barcode, image):
        food = FOOD()
        food.expiration_date = expiration_date
        food.weight = weight
        food.short_name = short_name
        food.long_name = long_name
        food.nutriscore_label = nutriscore_label
        food.segment_name = segment_name
        food.barcode = barcode
        food.image = image
        return food