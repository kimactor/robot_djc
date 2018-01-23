#!/usr/bin/env python3
from bottle import get,post,run,request,template

a=[0,0]
@get("/")
def index():
    return template("index")
@post("/cmd")
def cmd():
        if((request.body.read().decode())=='stop'):
            a[0]=1
        elif((request.body.read().decode())=='up'):
            a[1]=1
        elif((request.body.read().decode())=='down'):
            a[1]=2
        elif((request.body.read().decode())=='left'):
            a[1]=3
        else:
            a[1]=4

@get("/record")
def record():
    return str(a[0])

@get("/state")
def state():
    return str(a[1])

@get("/reset")
def reset():
    global a
    a=[0,0]
    return str(0)


run(host="0.0.0.0")

