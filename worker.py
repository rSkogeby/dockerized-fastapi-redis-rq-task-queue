import time


def runTask():
    print('starting runTask') # in place of actual logging

    time.sleep(5) # simulate long running task
    print('finished runTask')
    return {'group_name': 'task complete'}
