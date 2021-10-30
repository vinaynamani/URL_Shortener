from re import L
from flask import Flask, render_template, request, jsonify, redirect
import random
import os
import ssl
import pymongo
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
from flask_shorturl import ShortUrl

user_name = "ghost"
password = "anonymous0708"
client = pymongo.MongoClient(f"mongodb+srv://ghost:{password}@cluster0.2bq0e.mongodb.net/myFirstDatabase?retryWrites=true&w=majority",
                             ssl_cert_reqs=ssl.CERT_NONE)
db = client["my_database"]
collect = db["url_logs"]


app = Flask(__name__)

#######################--- SQLITE ORM ---##########################

# basedir = os.path.abspath(os.path.dirname(__file__))
# path = "sqlite:///"+os.path.join(basedir, "data.sqlite")
# app.config["SQLALCHEMY_DATABASE_URI"] = path
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

#######################--- SQLITE ORM ---##########################

s_url = ShortUrl(app)

#######################--- SQLITE ORM ---##########################

# db = SQLAlchemy(app)
# Migrate(app, db)

# class url_shortner(db.Model):
#     __tablename__ = "urltable"
#     id = db.Column("ID", db.Integer, primary_key=True)
#     short_url = db.Column(db.String(100))
#     long_url = db.Column(db.String(50))

#     def __init__(self, short_url, long_url):
#         self.short_url = short_url
#         self.long_url = long_url

#######################--- SQLITE ORM ---##########################


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/", methods=["POST"])
def shorten():
    if request.method == "POST":
        long_url = request.form.get("long_url")
        url = s_url.encode_url(len(long_url))
        short_url = "http://127.0.0.1:5000/"+str(url)
        list_of_urls = {"short_url": short_url, "long_url": long_url}
        collect.insert_one(list_of_urls)
        # new_url = url_shortner(short_url=short_url, long_url=long_url)
        # db.session.add(new_url)
        # db.session.commit()
        return render_template("index.html", short_url=short_url)


@app.route("/history")
def history():
    data_mongo = collect.find()
    data_mongo = list(data_mongo)
    # data = url_shortner.query.all()
    return render_template("history.html", urls=data_mongo)


@app.route("/<link>")
def direct(link):
    data_mongo = collect.find()
    data_mongo = list(data_mongo)
    for i in data_mongo:
        if i.get("short_url") == ("http://127.0.0.1:5000/"+link):
            return redirect(i.get("long_url"))


if __name__ == "__main__":
    app.run(debug=True)
