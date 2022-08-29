import asyncio
import requests
import datetime
import json

def Main():
    print("Program start ...... ")
    time = datetime.datetime.now()
    unitime = int(time.timestamp())
    nextime = unitime + 1
    print("nexttime : " + str(nextime))
    while(True):
        time = datetime.datetime.now()
        unitime = int(time.timestamp())
        if(nextime <= unitime):
            nextime = unitime + 1
            loop = asyncio.get_event_loop()
            loop.run_until_complete(Get(time))

async def  Get(time):
    data = await GetData(time)
    jdata = json.loads(data)
    if(not jdata["region_name"] == ""):
        await Send(data)
    else:
        print("CheckTime : " + str(time))

async def GetData(time):
    now = time.strftime('%Y%m%d%H%M%S')
    url = "http://www.kmoni.bosai.go.jp/webservice/hypo/eew/" + now + ".json"
    data = requests.get(url)
    return data.text

def Send(data):
    url = ""
    res = requests.get(url + data)
    print( res.status_code )

if __name__ == "__main__":
    Main()