import tornado.ioloop
import tornado.web

from fairdrop.auth import auth
import time

class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        token = self.get_secure_cookie("token")
        if token is not None:
            token = token.decode('utf-8')
            if auth.db.is_token_auth(token):
                return auth.db.get_address(token)
            
        return ""

def ts_to_human_delay(ts):
    delta = time.time() - ts
    if delta // 86400:
        return "{} days".format(int(delta // 86400))
    if delta // 3600:
        return "{} hours".format(int(delta // 3600))
    if delta // 60:
        return "{} minutes".format(int(delta // 60))

class AuthHandler(tornado.web.RequestHandler):
    def nonce(self):
        request = self.request.body.decode("utf-8")
        print(request)
        self.write(auth.get_nonce_response(request, as_json=False))

    def authentication(self):
        request = self.request.body.decode("utf-8")
        print(request)
        self.write(auth.get_authentication_response(request, as_json=False))

    def post(self, command):
        print(command, self.request.uri)
        if command:
            getattr(self, command.split("/")[0])()

    def get(self, command=""):
        if not command:
            url, token = auth.get_dna_url(get_token=True)
            self.set_secure_cookie("token", token)
            self.redirect(url)
        elif "logout" in command:
            self.set_secure_cookie("token", "")
            self.redirect("/")


class MainHandler(BaseHandler):
    def main(self):
        self.render("home.html")

    def index3(self):
        self.render("index3.html")


    def profile(self):
        if not self.current_user:
            self.redirect("/auth/")
            return
        status = auth.db.get_address_status(self.current_user)
        messages = auth.db.get_messages(self.current_user)
        self.render("profile/home.html", STATUS=status, MESSAGES=messages, ts_to_human_delay=ts_to_human_delay)

    def get(self, command=""):
        if not command:
            command = "main"
        getattr(self, command)()


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [(r"/auth/(.*)", AuthHandler), (r"/(.*)", MainHandler)]
        settings = dict(
            template_path="fairdrop/server/templates/",
            cookie_secret="generate a random value"
        )
        super(Application, self).__init__(handlers, **settings)


def start(port=8888):
    app = Application()
    app.listen(port)
    tornado.ioloop.IOLoop.current().start()