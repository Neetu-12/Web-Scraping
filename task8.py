import requests
import os
import json
from task1 import scrap_top_list
t1=scrap_top_list()
with open("task1.json","r+") as file:
    a=json.load(file)
def  txt():
    for i in a:
        path="/home/admin123/Documents/task8"+i["Name"]+".text"
        if os.path.exists(path):
            pass
        else:
            create=open("/home/admin123/Documents/task8"+i["Name"]+".text","w")
            url=requests.get(i["Url"])
            create1=create.write(url.text)
            create.close()
txt()