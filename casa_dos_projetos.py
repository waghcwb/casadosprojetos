__author__ = 'Joelson,wagner'
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.options import options
import uuid
import base64
import os


class configHandler(tornado.web.RequestHandler):
    def title(self):
        return 'Casa dos projetos'



class MainHandler(configHandler):
    def get(self):
        self.render('index.html',
                    title=self.title()
                    )

class AdminHandler(configHandler):
    def get(self):
        self.render('admin.html',
                    title=self.title()+' - Administrador')


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", MainHandler),
            (r"/admin", AdminHandler)
        ]
        settings = dict(
            blog_title=u"Casa dos projetos",
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            xsrf_cookies=False,
            cookie_secret=base64.b64encode(uuid.uuid4().bytes + uuid.uuid4().bytes),
            debug=True,
            default=80,
            autoreload=True,
        )
        tornado.web.Application.__init__(self, handlers, **settings)


def main():
    ip = '127.0.0.1'
    port = 80
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(port, ip)
    print('Running ', 'http://'+ip+':'+str(port))
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()