import requests
from config import BOT_TOKEN, GUILD_IDS
code = input("Enter authorization code: ")
def add_user_to_server(token: str, user_id: str, server_id: str, access_token: str) -> bool:
    url = f'https://discordapp.com/api/v8/guilds/{server_id}/members/{user_id}'
    headers = {
        'Authorization': f'Bot {token}'
    }

    data = {
        "access_token": access_token
    }

    response = requests.put(url, headers=headers, json=data)
    if response.status_code == 201:
        print(f'User {user_id} added to server with ID {server_id}')
        return True
    else:
        print(f'Error adding user {user_id} to server with ID {server_id}')
        return False

url = 'https://discord.com/api/users/@me'
headers = {'Authorization': f'Bearer {code}'}
response = requests.get(url, headers=headers).json()
user_id = response['id']
for GUILD_ID in GUILD_IDS:
    add_user_to_server(BOT_TOKEN, user_id, GUILD_ID, code)
