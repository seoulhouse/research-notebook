import json
import requests 
from process import getIdAndType, getSubInfo, toJson
from util import compose

def crawlerMainJob(*params):
    return compose(
        lambda data : getSubInfo(data, 650),
        getIdAndType,
        toJson,
        requests.get,
    )(*params)

def crawler(event, context):
    itemURL = 'https://apis.zigbang.com/v3/items2'
    itemURLPayload = {'lat_south': 37.44033750792432, 'lat_north': 37.6917904425295, 'lng_west': 126.87271708120215, 'lng_east': 127.08344785550588, 'room': '[01,02,03,04,05]'}
    
    data = crawlerMainJob(itemURL, itemURLPayload)
    
    response = {
        "statusCode": 200,
        "body": json.dumps(data)
    }
    return response
    
if __name__ == "__main__":
    crawler(1,1)