import os
import requests
import urllib.parse
from dotenv import load_dotenv


load_dotenv() # Carregar variáveis

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
REDIRECT_URI = os.getenv("REDIRECT_URI")

AUTH_URL = "https://accounts.spotify.com/authorize" # autoriza
TOKEN_URL = "https://accounts.spotify.com/api/token" # gera o token

