import json
data=open("task5.json","r")
d=json.load(data)
def analyse_movies_genre(movies_list):
    genre_list=[]
    dic={}
    for i in d:
        if "Genre" in i:
            genre=i["Genre"]
            for j in genre:
                if j in genre:
                    if j!="Other,":
                        if j!="Comedy,":
                            genre=j
                            dic[j]=1
                elif j in dic:
                    dic[j]+=1
        else:
            continue
    genre_list.append(dic)
    with open("task11.json","w") as file:
        json.dump(genre_list,file,indent=4)
analyse_movies_genre(d)