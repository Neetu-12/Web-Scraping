import json
from task1 import scrap_top_list
from task4 import scrap_movie_details
movie=scrap_top_list()
def get_movies_details(movie):
        details=[]
        for i in movie:
                details.append(scrap_movie_details(i["Url"]))
        with open("task5.json","w+") as file:
                json.dump(details,file,indent=4)
                return details
movie_detail=get_movies_details(movie[:10])


