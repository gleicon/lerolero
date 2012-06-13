from bottle import get, run, debug, abort, request, ServerAdapter, template, static_file
from lerolero import sayit

import os, json
STATIC_ROOT_PATH = "./static/"

@get('/')                                                                     
@get('/index.html')                                                           
@get('/static/<filename:path>')                        
def send_file(filename='index.html'):                                         
    return static_file(filename, root=STATIC_ROOT_PATH)     

@get('/wadl.xml')
def wadl():
    return static_file("wadl.xml", root=STATIC_ROOT_PATH)

@get('/lerolero')
def lero():
    i = sayit()
    return i

run(server='gevent', port=os.environ.get('PORT', 5000), host="0.0.0.0")
