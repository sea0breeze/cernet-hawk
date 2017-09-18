#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import session, flash

from orm.servicesinfo import ServicesInfo

app = Flask(__name__)

app.secret_key = 'sLdSPRk4OjrYkP2r8OIvhMGfTxL0mdAH'


@app.route('/')
def index():
    return render_template('index.html')


@app.route("/search/<searchStr>", methods=['GET'])
def search(searchStr=""):
    t = searchStr.split("=")
    if len(t) == 2:
        return errormsg("illegal search str")
    elif t[0] not in ["ip", "services", "port"]:
        return errormsg("illegal search str")

    if t[0] == "ip":
        return okmsg(ServicesInfo.searchByIP(t[1]))
    elif t[0] == "services":
        return okmsg(ServicesInfo.searchByName(t[1]))
    elif t[0] == "port":
        return okmsg(ServicesInfo.searchByPort(t[1]))


@app.route("/detail/<ip>", methods=['GET'])
def detail(ip=""):
    return okmsg(ServicesInfo.getDetailByIP(ip))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7682, debug=True)
