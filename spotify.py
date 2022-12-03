# Credentials you get from registering a new application
from requests_oauthlib import OAuth2Session
from requests.auth import HTTPBasicAuth
from os import environ

client_id = environ.get('SPOTIFY_CID') 
client_secret = environ.get('SPOTIFY_CLIENT_SECRET')
redirect_uri = 'https://twitter.com'

# OAuth endpoints given in the Spotify API documentation
# https://developer.spotify.com/documentation/general/guides/authorization/code-flow/
authorization_base_url = "https://accounts.spotify.com/authorize"
token_url = "https://accounts.spotify.com/api/token"

# https://developer.spotify.com/documentation/general/guides/authorization/scopes/
scope = [
    "user-read-email",
    "playlist-read-collaborative"
]
spotify = OAuth2Session(client_id, scope=scope, redirect_uri=redirect_uri)

# Redirect user to Spotify for authorization
authorization_url, state = spotify.authorization_url(authorization_base_url)
print('Please go here and authorize: ', authorization_url)

# Get the authorization verifier code from the callback url
redirect_response = input('\n\nPaste the full redirect URL here: ')
auth = HTTPBasicAuth(client_id, client_secret)

# Fetch the access token
token = spotify.fetch_token(token_url, auth=auth, authorization_response=redirect_response)
print(token)

# Fetch a protected resource, i.e. user profile
r = spotify.get('https://api.spotify.com/v1/me')
print(r.content)
