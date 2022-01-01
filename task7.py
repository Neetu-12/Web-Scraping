import json
with open("task5.json","r") as file:
    data=json.load(file)

def analyse_movies_directors(data):
    l=[]
    r={}
    for i in data:
        if "Director" in i:
            Director=i["Director"]
            for j in Director:
                if j not in r:
                    Director=i["Director"]
                    r[j]=1
                else:
                    r[j]+=1
        else:
            continue
    l.append(r)
    with open("task7.json","w+") as file:
        json.dump(l,file,indent=4)
        return l
print(analyse_movies_directors(data))
