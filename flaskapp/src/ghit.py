import os
import redis

global rh

def connect():
    global rh
    #rurl = os.getenv('REDISURL', 'redis://redis:6379')
    rurl = os.getenv('REDISURL')
    rh = redis.from_url(rurl)
    
def incr(key):
    global rh
    return rh.incr(key)

connect()
