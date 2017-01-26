'''
AREV - Backend Server
Author: Yuya Jeremy Ong (yuyajeremyong@gmail.com)
'''
import os
import json
import logging
import tornado.web
import tornado.websocket
import tornado.httpserver
import tornado.ioloop
from tornado.options import define, options, parse_command_line

# Logging and Command Line Arguments
logging.basicConfig(format='%(asctime)s [%(levelname)s] %(message)s')
define("port", default=9892, help="Initialize socket server on the given port", type=int)

# WebSocket Event Handler
class WebSocketHandler(tornado.websocket.WebSocketHandler):
    def check_origin(self, origin):
        return True

    def open(self):
        logging.info('[INFO]: WebSocket Connection Initialized')

        # Initialize Handshake

    def on_message(self, message):
        try:
            print message
            packet = json.loads(message)
            print packet
        except:
            print 'error handling packet'
            # return self.write_message(self.create_packet('status', "Error parsing incoming packet."))

    def on_close(self):
        logging.info('[INFO]: WebSocket Connection Closed')

# Static Front-End Dashboard Handler


# Server Application Class
class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            # (r'/', IndexPageHandler),
            (r'/ws', WebSocketHandler)
        ]

        settings = { 'template_path': 'templates' }
        tornado.web.Application.__init__(self, handlers, **settings)

if __name__ == '__main__':
    parse_command_line()

    # Initialize Server
    server = tornado.httpserver.HTTPServer(Application())
    server.listen(options.port)

    logging.info('[INFO]: Initialized websocket server at ws://127.0.0.1:'+str(options.port)+'/ws')

    # Initialize IO Event Handler Loop
    tornado.ioloop.IOLoop.instance().start()
