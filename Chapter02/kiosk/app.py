import os
from time import time
from flask import Flask, request
from flask_redis import FlaskRedis

app = Flask(__name__)
app.config['REDIS_URL'] = "redis://{0}:{1}/{2}".format(
    os.environ.get('REDIS_HOST', 'localhost'),
    os.environ.get('REDIS_PORT', '6379'),
    os.environ.get('REDIS_DB', '0')
)
redis_store = FlaskRedis(app)


@app.route('/tickets', methods=['POST'])
def set_tickets():
    new_ticket_counts = request.form.get('value')
    if new_ticket_counts is not None:
        redis_store.set('tik', new_ticket_counts)
        return 'SUCCESS'
    else:
        return 'NOTHING UPDATED'


@app.route('/tickets', methods=['GET'])
def get_tickets():
    return redis_store.get('tik') or '0'


@app.route('/buy', methods=['POST'])
def buy_a_ticket():
    with redis_store.pipeline() as pipe:
        while True:
            try:
                ret = 'NO TICKETS'
                pipe.watch('tik')
                if int(pipe.get('tik') or 0):
                    pipe.decr('tik')
                    # send a log to pub chanell
                    pipe.publish(
                        'selling_timestamp',
                        '{0}'.format(int(1000 * time())))
                    ret = 'SUCCESS'
                pipe.execute()
                break
            except Exception as ex:
                continue
    return ret

if __name__ == "__main__":
    app.run(host="0.0.0.0")
