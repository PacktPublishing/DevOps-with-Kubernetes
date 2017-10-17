import os
import signal
import time
import threading
from http.server import (
    BaseHTTPRequestHandler,
    HTTPServer
)


def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


class MyMsgHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        try:
            message = str(fib(int(self.path.split('/')[1])))
        except ValueError as ex:
            message = "OK"
        self.send_response(200)
        self.end_headers()
        self.wfile.write(message.encode())
        return

    def do_HEAD(self):
        self.send_response(200)
        self.end_headers()
        return

    def log_message(self, format, *args):
        print("{0:6f} - {1}".format(time.time(), *args))
        return


class MyApp(object):

    def __init__(self):
        self.httpd = HTTPServer(('0.0.0.0', 5000), MyMsgHandler)

    def run(self):
        print('starting server at {0:6f}'.format(time.time()))
        self.httpd.serve_forever()

    def stop(self):
        print('stopping server at {0:6f}'.format(time.time()))
        threading.Thread(target=self.httpd.shutdown).start()

if __name__ == '__main__':
    def graceful_exit_handler(signum, frame):
        app.stop()
    app = MyApp()
    signal.signal(signal.SIGTERM, graceful_exit_handler)
    app.run()
