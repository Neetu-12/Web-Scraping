import json
with open("task2.json","r+") as file:
    data=json.load(file)
def group_by_decade(movies):
    moviedec={}
    list=[]
    for index in movies:
        mod=int(index)%10
        decade=int(index)-mod
        if decade not in list:
            list.append(decade)                     
    list.sort()
    for i in list:
        moviedec[i]=[]
    for i in moviedec:
        dec10=i+9
        for x in  movies:
            if int(x)<=dec10 and int(x)>=i:
                for v in movies[x]:
                    moviedec[i].append(v)
    with open("task3.json","w+") as file:
        json.dump(moviedec,file,indent=4)
        return moviedec
group_by_decade(data)