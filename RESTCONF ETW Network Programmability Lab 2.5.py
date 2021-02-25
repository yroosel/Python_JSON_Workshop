import json
import requests
requests.packages.urllib3.disable_warnings()
print("Starting RESTCONF Application")
print('------1-------')
print("=> Creating request URL")
api_scheme = "https://"
api_authority = "192.168.56.101" # change ip address if necessary
api_path = "/restconf/data/ietf-interfaces:interfaces"
# api_url = "https://192.168.56.101/restconf/data/ietf-interfaces:interfaces"
api_url = api_scheme + api_authority + api_path
print(api_url)
print('------2-------')
print("=> Creating connection parameters for data exchange")
headers = { "Accept": "application/yang-data+json", 
            "Content-type":"application/yang-data+json"
          } 
print(headers)
print(type(headers))
print('------3-------')
print("=> Creating authentication & authorization parameters")
basicauth = ("cisco", "cisco123!")
print(basicauth)
print(type(basicauth))
print('------4-------')
print("=> Sending GET request with defined parameters")
resp = requests.get(api_url, auth=basicauth, headers=headers, verify=False)
print(resp.status_code)
print('------5-------')
print("=> Handling HTTP Response")
response_json = resp.json()
print('------6-------')
print("=> Printing raw response")
print(response_json) 
print('------7-------')
print("=> Printing pretty response")
print(json.dumps(response_json, indent=2))
print('------8-------')
print("=> Printing filtered response")
#print(dir(response_json["ietf-interfaces:interfaces"]))
print('------9-------')
print("Interface Name: ")
print(response_json["ietf-interfaces:interfaces"]["interface"][1]["name"])
print('------10-------')
print("IP Address + Subnet: " )
ip_subnet = response_json["ietf-interfaces:interfaces"]["interface"][1]["ietf-ip:ipv4"]["address"]#["ip"]
print(ip_subnet)
print('------11-------')
print("IP Address: " )
ip = response_json["ietf-interfaces:interfaces"]["interface"][1]["ietf-ip:ipv4"]["address"][0]["ip"]
print(ip)

