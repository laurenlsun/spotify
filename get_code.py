from dotenv import load_dotenv
from flask import Flask, render_template, redirect
import os

load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/submit_client", methods=["POST", "GET"])
def produce_code():
    return redirect(get_verif_url(client_id))


def get_verif_url(client_id):
    url = "https://accounts.spotify.com/authorize"
    url += "?client_id=" + client_id
    url += "&response_type=code"
    url += "&redirect_uri=http://127.0.0.1:5000/"
    url += "&show_dialog=true"
    url += "&scope=playlist-modify-private playlist-modify-public"
    return url


def main():
    app.secret_key = os.urandom(12)
    app.run()

if __name__=="__main__":
    main()