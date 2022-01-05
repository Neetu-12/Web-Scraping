import json
with open("task5.json","r") as file:
    d=json.load(file)
a=d[:48]

def get_movies_details(movie):
    details={}
    for i in movie:
        for d in i["Director"]:
            details[d]={}
    for i in range(len(movie)):
        for d in details:
            if d in movie[i]["Director"]:
                l=movie[i]["Language"]
                details[d][l]=0
    for i in range(len(movie)):
        for d in details:
            if d in movie[i]["Director"]:
                l=movie[i]["Language"]
                details[d][l]+=1
       
    with open("task10.json","w+") as file:
            json.dump(details,file,indent=4)
            return details
movie_detail=get_movies_details(a)



import json
with open("task5.json","r") as file:
    d=json.load(file)
a=d[57:]

def neetu(movie):
    details={}
    for i in movie:
        for d in i["Director"]:
            details[d]={}
    for i in range(len(movie)):
        for d in details:
            if d in movie[i]["Director"]:
                l=movie[i]["Language"]
                details[d][l]=0
    for i in range(len(movie)):
        for d in details:
            if d in movie[i]["Director"]:
                l=movie[i]["Language"]
                details[d][l]+=1
       
    with open("task10.json","w+") as file:
            json.dump(details,file,indent=4)
            return details
movie_detail=neetu(a)
