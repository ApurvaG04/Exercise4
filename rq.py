import requests
from redis import Redis
from rq import Queue
from my_module import count_words_at_url
from rq import Retry


def count_words_at_url(url):
    resp = requests.get(url)
    return len(resp.text.split())
    
q = Queue(connection=Redis())
result = q.enqueue(count_words_at_url, 'http://nvie.com')
