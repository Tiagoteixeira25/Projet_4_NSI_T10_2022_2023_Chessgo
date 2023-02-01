# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 08:15:42 2023

@author: teixeira
"""

from flask import *
import datetime

app = Flask(__name__)

@app.route('/')

def accueil():
    return render_template("untitled3.html")

@app.route('/heure')

def heure():
    date_heure=datetime.datetime.now()
    h = date_heure.hour
    m = date_heure.minute
    s = date_heure.second
    print(h,m,s)
    return render_template("untitled4.html", heure=h,minute=m,second=s)



if __name__ == "__main__":
    app.run(debug = True)