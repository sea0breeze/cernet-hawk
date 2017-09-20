#!/usr/bin/env python
# -*- coding:utf-8 -*-

import tornado.options
import tornado.ioloop
import tornado.web
import tornado.wsgi
import wsgiref.simple_server

from config.common import DEBUG
from config.websrv import settings
from config.websrv import handlers


def main():
    try:
        app = tornado.web.Application(handlers, debug=DEBUG, **settings)
        print("[*] Server run at %s" % tornado.options.options.url)

        if True:
            app.listen(tornado.options.options.port)
            tornado.ioloop.IOLoop.instance().start()
        else:
            # reserve for wsgi
            server = wsgiref.simple_server.make_server('', 8888, app)
            server.serve_forever()
    except Exception as e:
        import traceback
        print(traceback.print_exc())
    finally:
        import sys
        sys.exit(0)

if __name__ == "__main__":
    main()
