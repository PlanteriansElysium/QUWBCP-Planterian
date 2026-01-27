# If cisco has 10 competitors i am one of them
# If cisco has one competitor it is me
# If cisco has no competitors i am dead
# made by planterian to check if cisco is out yet

import requests #http/s requests library
def data_get(team_number):
    url = "https://scoreboard.uscyberpatriot.org/api/team/scores.php" # URL for API with teams endpoint
    parameters = {"team[]":team_number}
    agentID = {
    "User-Agent": "https://github.com/PlanteriansElysium/QUWBCP-Planterian# by plantofelysium@gmail.com" #hello there its a me mario (planterian)
}


    try:
        response = requests.get(url, params= parameters, headers= agentID) #sends request to api
        response.raise_for_status() #bad status code checker (4xx-5xx)
        return response.json()
    except requests.exceptions.Timeout: #message timeout
        print("the request has timed out")
    except requests.exceptions.RequestException as e:
        print(f"an error has occured: {e}") #tells user if error is found
        return None
    
if __name__ == "__main__": 
    teamnum = "18-0218" #can be made a user input for other uses
    teamData = data_get(teamnum)
    if teamData:
        print(f"Data for team {teamnum}:") #api returns object with a bunch of data

        if "data" in teamData and isinstance(teamData["data"], list) and len(teamData["data"]) > 0: #checks if the data is normal (not bugged)
            team_info = teamData["data"][0]
            print (f"Team number: {team_info.get('team_number')}")
            print (f"play Time: {team_info.get('play_time')}")
            print (f"Score Time: {team_info.get('score_time')}")
            print (f"CCS Score: {team_info.get('css_score')}")
            print (f"Location: {team_info.get('location')}")
            print (f"Division: {team_info.get('division')}")
            print (f"Tier: {team_info.get('tier')}")
            print (f"Total score: {team_info.get('total')}")
            print (f"c1: {team_info.get('score_1')}")
            print (f"c2: {team_info.get('score_2')}")
            print (f"c3: {team_info.get('score_3')}")
          

