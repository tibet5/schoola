import os
import flask
import schoola.settings

#  Generate a class inherited from 'flask' object, to make ourselves able to use different server drivers
#  for the case it would be needed.
#  Mark the root project folder as instance of 'Flask'.
#  Take the first directory for setting it the main flask dir.
#  Declare template and static folders according to this first directory.
#  Like < teplate_folder = schoola.templates >
class FlaskDriver(object):
    def __init__(self, *args, **kwargs):
        self.instance = flask.Flask(
            __name__.split('.')[0],
            template_folder=os.path.join('templates'),
            static_folder=os.path.join('static'),
        )

#  Prepares the shape of route for flask canonical rules by using flasks add url rule function.
#  Controller class added as element of optional variadic
    def add_route(self, name, path, methods, controller_class):
        wrapped_controller = self.wrap_controller(
            name,
            controller_class,
        )
        self.instance.add_url_rule(
            path,
            name,
            wrapped_controller,
            methods=methods,
        )

#  Prepare and wrapped the given controller-model in appropriate way for flask's render template.
#  It was necessary shaping the model in right form to make it viewable.
#  Each custom controller will be wrapped by this function for being able to use flasks requests etc..
    def wrap_controller(self, name, controller_class):
        def controller_wrapper(*args, **kwargs):
            from flask import request
            controller = controller_class(
                request=request,
                route_name=name,
                render_template=self._render_template
            )
            return controller.handle_request(*args, **kwargs)
        return controller_wrapper
#  This works same as flasks render template func. But it is private now to this project.
    def _render_template(self, template_name, **kwargs):
        return flask.render_template(template_name, **kwargs)
#  Instance is this flask app now. It is same with saying run this app with debug mode on.
    def start(self):
        self.instance.run(
            debug=schoola.settings.DEBUG,
        )
