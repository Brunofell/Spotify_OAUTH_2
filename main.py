import os
import requests
import urllib.parse
from dotenv import load_dotenv


load_dotenv() # Carregar variáveis

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
REDIRECT_URI = os.getenv("REDIRECT_URI")

# urls do spotify
AUTH_URL = "https://accounts.spotify.com/authorize"
TOKEN_URL = "https://accounts.spotify.com/api/token"
API_URL = "https://api.spotify.com/v1/me"


def generate_link():
    params = {
        "client_id": CLIENT_ID,
        "response_type": "code",
        "redirect_uri": REDIRECT_URI
    }
    
    query = urllib.parse.urlencode(params)
    
    return f"{AUTH_URL}?{query}"
    

def get_token(code):
    data = {
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": REDIRECT_URI,
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET
    }
    
    response = requests.post(TOKEN_URL, data=data)
    
    return response.json()


def call_api(token):
    headers = {
        "Authorization": f"Bearer {token}"
    }
    
    response = requests.get(API_URL, headers=headers)
    return response.json()


def main():
    
    # Passo 1: Login
    link = generate_link()

    print("\nOpen Browser: \n")
    print(link)

    # Passo 2: receive code
    code = input("\nPaste the URL code here: ").strip()

    # Passo 3: get token
    token_data = get_token(code)

    access_token = token_data["access_token"]

    print("\nToken received!")

    # 4: Call API
    dados = call_api(access_token)

    print("\User data:\n")
    print(dados)


main()
    
    
    
    
