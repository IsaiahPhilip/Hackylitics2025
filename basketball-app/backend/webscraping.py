
from bs4 import BeautifulSoup
import requests
#Work on this later 

# get's the player information based on the url 
def get_player_info(name): 
    
    url = "https://www.nba.com/player/203500/" + name

    #If information does not appear then use chat response
    return url