import requests
import json
from  bs4 import BeautifulSoup
url="https://www.rottentomatoes.com/top/bestofrt/top_100_animation_movies/"
sample = requests.get(url)
soup = BeautifulSoup(sample.text,"html.parser")
def scrap_top_list():
    r=[]
    maindiv=soup.find("div", class_="panel-body content_body allow-overflow")
    n=maindiv.find("table",class_="table")
    b=n.find_all("tr")
    for i in b:
        d={}
        td=i.find_all("td")
        for j in td:
            rank=i.find("td",class_="bold").get_text()[:-1]
            d["Rank"]=int(rank)
            rating=i.find("span",class_="tMeterScore").get_text()[:-1]
            d["Rating"]=float(rating)
            review=i.find("td",class_="right hidden-xs").get_text()
            d["Review"]=int(review)
            name=i.find("a",class_="unstyled articleLink")["href"][3:]
            d["Name"]=str(name)
            movie_url=i.find("a",class_="unstyled articleLink")["href"]
            url="https://www.rottentomatoes.com"+ movie_url
            d["Url"]=url
            year=i.find("a",class_="unstyled articleLink").get_text()
            y=year.strip()
            d["Year"]=int(y[-5:-1])
        r.append(d)
        if {} in r:
            r.remove({})
    with open("task1.json","w+") as file:
        json.dump(r,file,indent=4)
        return r

scrap_top_list()