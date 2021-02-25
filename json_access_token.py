#### DEVASC LAB 3.6.6
import json
atk = {
 "access_token":"ZDI3MGEyYzQtNmFlNS00NDNhLWFlNzAtZGVjNjE0MGU1OGZmZWNmZDEwN2ItYTU3",
 "expires_in":1209600,
 "refresh_token":"MDEyMzQ1Njc4OTAxMjM0NTY3ODkwMTIzNDU2Nzg5MDEyMzQ1Njc4OTEyMzQ1Njc4",
 "refreshtokenexpires_in":7776000
}
print('-----1-----')
print (type(atk))
print('-----1B-----')
print(atk.keys())
print('-----2-----')
#### pretty output
print(json.dumps(atk, indent=8))
#### FILTERING DATA
#### filter access-token
print('-----3-----')
print(atk["access_token"])
#### TRANSFORMING DATA TYPES
print('-----4-----')
ats = json.dumps(atk)  #### SERIALIZATION
print(type(ats))
####
print('-----5-----')
atj = json.loads(ats)
print(type(atj))
