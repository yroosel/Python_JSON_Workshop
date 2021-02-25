### ADD NEW SPACES AND MEMBERS TO WEBEX TEAMS
### USING THE JSON STRUCURE CREATED BY DEVASC JSON Webex Teams Groups and Users from Excel.py
### Access Token 12 hours: https://developer.webex.com/docs/api/getting-started (login required)
current_access_token = "Njk3...04fe45ea181f"
###
import requests
import json
###
from webexteamssdk import WebexTeamsAPI
api = WebexTeamsAPI(access_token=current_access_token)
###
import datetime
print("Creating spaces +  members --> from Excel spreadsheet in the previous cell")
print ("Current date and time: ")
print(datetime.datetime.now())
access_token = current_access_token 

def main2(): # using rest api
    url = 'https://api.ciscospark.com/v1/rooms'
    headers = {'Authorization': 'Bearer {}'.format(access_token),'Content-Type': 'application/json' }
    for rec in groups_struc["groups"]:
        create_group_name = rec["group"]["group_name"]
        payload_space={"title": create_group_name}
        if payload_space["title"] != None:  ### avoid errors if room title is unknown
            res_space = requests.post(url, headers=headers, json=payload_space)
            #print(payload_space)
            #print(res_space.text)
            if res_space.status_code < 300:
                NEW_SPACE_ID = res_space.json()["id"]
                #print(type(NEW_SPACE_ID))
                #print(NEW_SPACE_ID)
                for mbr in rec["group"]["members"]:
                    room_id = NEW_SPACE_ID
                    person_email = mbr["email"] 
                    url2 = 'https://api.ciscospark.com/v1/memberships'
                    payload_member = {'roomId': room_id, 'personEmail': person_email}
                    #print(payload_member)
                    res_member = requests.post(url2, headers=headers, json=payload_member)

def main():  # using webxteamssdk
    for rec in groups_struc["groups"]:
        # Create a new demo room
        demo_room = api.rooms.create(rec["group"]["group_name"])
        # Add people to the new demo room
        for email in rec["group"]["members"]:
            api.memberships.create(demo_room.id, personEmail=email["email"])

#### execute main() when called directly        
if __name__ == "__main__":
    main2()  
