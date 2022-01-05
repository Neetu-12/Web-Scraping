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
    with open("task12.json","w") as file:
        json.dump(l1,file,indent=4)

cast(di)

