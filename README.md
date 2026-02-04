# 🎵 Spotify OAuth Authentication with Python

This project is a **simple educational implementation** of Spotify's
OAuth 2.0 Authorization Code Flow using Python.

The main goal is to understand, in practice, how authentication works
before using APIs in real data engineering pipelines.

------------------------------------------------------------------------

## 📌 Project Goals

-   Understand how OAuth 2.0 works in practice
-   Learn how to authenticate with external APIs
-   Practice secure credential management
-   Prepare for integration with data pipelines
-   Learn how access tokens are generated and used

------------------------------------------------------------------------

## 🛠️ Technologies Used

-   Python 3.12+
-   Requests
-   python-dotenv
-   Spotify Web API
-   OAuth 2.0

------------------------------------------------------------------------

## 📂 Project Structure

    spotify-oauth-basic/
    ├── main.py
    ├── .env
    ├── .gitignore
    └── README.md

------------------------------------------------------------------------

## 🔐 Spotify App Configuration

### Create App

1.  Go to https://developer.spotify.com/dashboard
2.  Login
3.  Click Create App
4.  Fill name and description

### Redirect URI

Use:

http://127.0.0.1:8080/callback

------------------------------------------------------------------------

## ⚙️ Environment Configuration

Create `.env` file:

CLIENT_ID=your_client_id\
CLIENT_SECRET=your_client_secret\
REDIRECT_URI=http://127.0.0.1:8080/callback

------------------------------------------------------------------------

## ▶️ How to Run

Install dependencies:

pip install requests python-dotenv

Run:

python main.py

------------------------------------------------------------------------

## 🔄 OAuth Flow

User → Login → Code → Token → API

------------------------------------------------------------------------

## 📖 Learning Outcomes

-   Understand OAuth 2.0
-   Learn token exchange
-   Secure credential management
-   API authentication

------------------------------------------------------------------------

## 🚀 Future Improvements

-   Refresh token
-   Automation
-   Airflow integration
-   AWS Secrets Manager

------------------------------------------------------------------------

## 👨‍💻 Author

Bruno Martins
