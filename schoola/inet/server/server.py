from schoola.inet.server.drivers import FlaskDriver
from schoola.inet.router import ROUTES

#  This class created to be an object which encapsulate the driver. In this case, the driver is Flask driver.
#  For the possibility we want to change framework.
#  Initialize server's driver as Flask. Add all and each route and its key and value have been specified in router.
#  For making them reachable by driver.
class Server(object):
    def __init__(self, *args, **kwargs):
        driver_class = kwargs.get('driver_class', FlaskDriver)
        self.driver = driver_class(*args, **kwargs)
        for route in ROUTES:
            self.add_route(
                route['name'],
                route['path'],
                route['methods'],
                route['controller_class']
            )

    def add_route(self, name, path, methods, controller_class):
        return self.driver.add_route(name, path, methods, controller_class)

#  This function reaches the flask drivers start function which runs the app.
    def start(self):
        return self.driver.start()
