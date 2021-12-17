from task1 import scrap_top_list
import json
scrapped=scrap_top_list()
def group_by_year(movies):
    years=[]
    for i in movies:
        year=i["Year"]
        if year not in years:
            years.append(year)
    d={}
    for i in years:
        for x in movies:
            if str(i)==str(x["Year"]):
                d[i]=[x]
    with open("task2.json","w+") as file:
        json.dump(d,file,indent=4)
        return d
print(group_by_year(scrapped))       