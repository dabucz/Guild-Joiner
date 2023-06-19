from flask import Flask, request
import requests
from config import *
app = Flask(__name__)

# The callback URL for OAuth2 authorization
@app.route('/auth/callback')
def callback():
    code = request.args.get('code')

    # Exchange the authorization code for an access token
    url = 'https://discord.com/api/oauth2/token'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    data = {
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': REDIRECT_URI,
        'scope': 'identify guilds.join'
    }
    response = requests.post(url, headers=headers, data=data).json()
    access_token = response['access_token']

    # Get the user ID from the access token
    url = 'https://discord.com/api/users/@me'
    headers = {
        'Authorization': f'Bearer {access_token}'
    }
    response = requests.get(url, headers=headers).json()
    user_id = response['id']

    print(f"authorization code: {access_token} to user {user_id}")
    with open(f'codes.txt', 'a+') as f:
        f.write(f'id: {user_id} | code: {access_token}\n')
    return f"Success"

if __name__ == '__main__':
    print("Auth bot url: https://discord.com/api/oauth2/authorize?client_id=908399065723699220&redirect_uri="+REDIRECT_URI+"&response_type=code&scope=guilds.join")
    app.run(debug=True, port=PORT, host=HOST)
