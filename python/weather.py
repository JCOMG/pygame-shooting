import requests
import json

def weatherStation( keyword):
    result = []
    page = 1
    payload = {'name': keyword, 'page': page}
    response = requests.get("https://jsonmock.hackerrank.com/api/weather/search", params= payload)
    total_page = response.json()['total_pages']
    while page <= total_page:
        for item in response.json()['data']:
            name = item['name']
            weather = item['weather'].split()[0]
            status = getStatusString(item['status'])
            result.append(name+","+weather+","+status)
        page+=1
    return result

def getStatusString( status):
    wind = status[0].split()[1].replace('Kmph','')
    humidity = status[1].split()[1].replace('%','')
    return wind +","+humidity

print(weatherStation('in'))