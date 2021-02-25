import time
import requests
import json

def get_token(host):
    """
    Gets an access token from Cisco DNA Center. Returns the token
    string if successful; raises HTTPError otherwise.
    """
    # Declare useful local variables to simplify request process
    auth = ("devnetuser", "Cisco123!")
    headers = {"Content-Type": "application/json"}
    # Issue HTTP POST request to the proper URL to request a token
    auth_resp = requests.post(
        f"https://{host}/dna/system/api/v1/auth/token",
        auth=auth,
        headers=headers,
    )
    # If successful, print token. Else, raise HTTPError with details
    auth_resp.raise_for_status()
    token = auth_resp.json()["Token"]
    return token

print('Requesting devices client health')
host = "sandboxdnac2.cisco.com"
token = get_token(host)

# Declare useful local variables to simplify request process
headers = {"Content-Type": "application/json", "X-Auth-Token": token}
# API requires specifying the epoch as query parameter. Take current
# time in epoch seconds, convert to ms, and remove decimal
# Note: epoch 0 = 00:00:00 UTC on 1 January 1970
current_epoch = int(time.time() * 1000)
params = {"timestamp": current_epoch}

# Issue HTTP GET request to get high-level client health
# f-string is used for string formatting
get_resp = requests.get(
    f"https://{host}/dna/intent/api/v1/client-health",
    headers=headers,
    params=params,
)

get_resp_json = get_resp.json()
print(get_resp_json)
#print(json.dumps(get_resp_json, indent=4))

# get-health timeout and number of times to attempt if timeout occurs
TIMEOUT = 10
ATTEMPTS = 3

host = "sandboxdnac2.cisco.com"
token = get_token(host)

headers = {"Content-Type": "application/json", "X-Auth-Token": token}

# API requires specifying the epoch as query parameter. Take current
# time in epoch seconds, convert to ms, and remove decimal
# Note: epoch 0 = 00:00:00 UTC on 1 January 1970
current_epoch = int(time.time() * 1000)
params = {"timestamp": current_epoch}

# Run the loop however many times is specified by ATTEMPTS
for i in range(ATTEMPTS):
    # Code in the "try" block may raise errors
    try:
        # Issue HTTP GET request to get high-level client health
        get_resp = requests.get(
            f"https://{host}/dna/intent/api/v1/client-health",
            headers=headers,
            params=params,
            timeout=TIMEOUT,
        )

        # Request succeeded, break out of loop early
        if get_resp.ok:
            break
    except requests.exceptions.ReadTimeout:
        # Catch error, print message, and quit the program
        # with error code 1 if we are on the last attempt
        print(f"Timeout {i+1}/{ATTEMPTS} ({TIMEOUT} sec)")
        if i + 1 == ATTEMPTS:
            print("Could not collect client health")
            import sys
            sys.exit(1)

# Convert HTTP response body to JSON to extract health data
get_resp_json = get_resp.json()
#print(get_resp_json)
print(json.dumps(get_resp_json, indent=2))

# Print JSON response for troubleshooting and learning
# import json; print(json.dumps(get_resp_json, indent=2))

#### FILTERING JSON RESPONSE DATA
print("----------1----------")
print(type(get_resp_json))
print("----------2----------")
print("Number of clients in first group")
print(get_resp_json["response"][0]["scoreDetail"][0]["clientCount"])
