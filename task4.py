import requests
import json
from bs4 import BeautifulSoup
url="https://www.rottentomatoes.com/m/spider_man_into_the_spider_verse"
def scrap_movie_details(movie_url):
    res=requests.get(movie_url)
    soup = BeautifulSoup(res.text,"html.parser") 
    h1=soup.find("h1", class_="scoreboard__title").get_text()
    li=soup.find_all("li",class_="meta-row clearfix")
    r={}
    r["Name"]=h1
    for i in li:
        a=i.text
        b=a.split()
        if "Rating:" in b:
            r["Rating"]=b[1]
        elif "Genre:" in b:
            r["Genre"]=b[1:]
        elif "Language:" in b:
            r[" Language"]=b[2]
        elif "Director:" in b:
            r["Director"]=b[0:]
        elif "Producer:" in b:
            r["Producer"]=b[1:]
        elif "Runtime:" in b:
            s=b[1:]
            for i in s:
                if "h" in i:
                    first=int(i[0:-1])*60
                elif "m" in i:
                    sec=int(i[:-1])
            r["Runtime"]=first+sec
    with open("task4.json","w+" ) as file:
        json.dump(r,file,indent=4)
        return r
(scrap_movie_details(url))