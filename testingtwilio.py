import requests
import base64
import json


# Spotify API credentials
CLIENT_ID = 'af57d6fc83e0485fb8b826f0cf55f3fd'
CLIENT_SECRET = '003c013537014b338a4c09ad0c83801b'

# Get an access token
def get_access_token(client_id, client_secret):
    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + base64.b64encode(f"{client_id}:{client_secret}".encode()).decode()
    }
    data = {
        "grant_type": "client_credentials"
    }
    response = requests.post(url, headers=headers, data=data)
    return response.json()["access_token"]

# Search for artists in Kenya
def search_artists_in_kenya(token):

    url = "https://api.spotify.com/v1/search"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    params = {
        "q": "genre:kenya",  # Search by genre keyword (adjust if needed)
        "type": "artist",    # Specify the search type
        "market": "KE",      # Specify the market (e.g., Tanzania or Kenya)
        "limit": 50
    }
    # Make the GET request
    response = requests.get(url, headers=headers, params=params)

    # Check for a successful response
    if response.status_code != 200:
        print(f"Error: {response.status_code}, {response.text}")
        return []

    # Parse the JSON response
    data = response.json()

    # Extract artist IDs
    return data 



def search_for_albums(token, id): 
    id = id 
    url = f"https://api.spotify.com/v1/artists/{id}/albums"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    params = {
        "q": "genre:kenya",
        "type": "album",
        "market": "KE",
        "limit": 10
    }
    response = requests.get(url, headers=headers, params=params)
    data_2_return = response.json()
    return json.dumps(data_2_return, indent=4)

def get_artist_from_list(token, artist_name): 
    data = search_artists_in_kenya(token) 
    # if data["items"]["artists"]["name"].lower() == artist_name.lower():
    #     print(data["items"]["name"])
    new_data = data["artists"]["items"]

    l = len(new_data)
    total_urls = []
    for i in range(l):
        if new_data[i]["name"].lower() == artist_name.lower():
            total_urls.append(new_data[i]["id"])

    return total_urls

def get_album_tracks(token, id): 
    url = f"https://api.spotify.com/v1/artists/{id}/top-tracks"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    params = {
        "q": "genre:kenya",
        "type": "album",
        "market": "KE",
        "limit": 10
    }
    response = requests.get(url, headers=headers, params=params)
    data = response.json()
    final_list = []
    for i in range(len(data["tracks"])): 
        final_list.append(data["tracks"][i]["album"]["name"])
    return final_list

# Main execution
access_token = get_access_token(CLIENT_ID, CLIENT_SECRET)
total_data = search_artists_in_kenya(access_token)


artist_list_of_names = []
for data in total_data:
    items = total_data[data]["items"]
    for i in range(len(items)):
        artist_list_of_names.append(items[i]["name"])


dict_of_top_songs = {}
for name in artist_list_of_names:
    new_id = get_artist_from_list(access_token, name)
    dict_of_top_songs[name] = get_album_tracks(access_token, new_id[0])

print(json.dumps(dict_of_top_songs, indent=4))