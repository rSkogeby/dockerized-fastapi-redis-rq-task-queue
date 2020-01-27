from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from redis import Redis
from rq import Queue

from worker import runTask

app = FastAPI()

redis_conn = Redis(host='myproj_redis', port=6379)
q = Queue('my_queue', connection=redis_conn)

@app.get('/hello')
def hello():
    """Test endpoint"""
    return {'hello': 'world'}


@app.post('/groups/group1', status_code=201)
def addTask():
    """
    Adds tasks to worker queue.
    Expects body as dictionary matching the Group class.
    """

    job = q.enqueue(runTask)
    size = len(q)

    return {'job': size}


@app.get('/queueSize')
def queueSize():
    """Test endpoint"""
    return {'Queue Size': len(q)}
