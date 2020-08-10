from redis import Redis
import rq
from rq import Connection, Worker

r = Redis(host='queue', port=6379, db=0)

with Connection(r):
    w = Worker(['default'])
    w.work()
