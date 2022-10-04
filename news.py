import requests

api_address = ('http://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey=5a35f4d051414e6298156a91866d913a')
json_data = requests.get(api_address).json()

ar=[]

def news():
    for i in range(4):
        ar.append("Number" + str(i+1) + " " + json_data["articles"][i]["title"] + json_data["articles"][i]["description"] + ".")
        
    return ar