import json
from task4 import movie_details
import json,requests,bs4
url="https://www.rottentomatoes.com/m/inside_out_2015"
req=requests.get(url)
soup=bs4.BeautifulSoup(req.text,"html.parser")
di=soup.find("div",class_="castSection")
def cast(main_div):
    l=[]
    for i in main_div:
        k=i.text
        b=k.split()

        i=0
        dic={}
        while i<len(b):
            a=b[0]+b[1]
            dic["cast_name"]=a
            i+=1
        l.append(dic)
    i=0
    l1=[]
    while i<len(l):
        if i%2!=0:
            l1.append(l[i])
        i+=1
    return l1
a=cast(di)
t4=movie_details(url)
def cast_details(data):
    dic=[]
    dic.append(data)
    for i in range(len(a)):
        dic.append(a[i])
    with open("task13.json","w+") as file:
        json.dump(dic,file,indent=4)
        return dic
print(cast_details(t4))
