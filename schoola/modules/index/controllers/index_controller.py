from schoola.arch.mvc import Controller


class IndexController(Controller):

    TITLE = 'Index'

    def handle_request(self):
        template_path = 'index/index.html'
        return self.render_template(template_path)
