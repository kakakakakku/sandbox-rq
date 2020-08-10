from rq import Queue
from redis import Redis
from job import count_words_at_url
import time

r = Redis(host='queue', port=6379, db=0)
q = Queue(connection=r)

job = q.enqueue(count_words_at_url, 'https://kakakakakku.hatenablog.com/')

time.sleep(5)
print(job.result)
