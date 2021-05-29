from schoola.persistence import Database


class CreateMixin(object):

    TEMPLATE_DIRECTORY_NAME = None

    MODEL_CLASS = None

    def handle_create_request(self, *args, **kwargs):
        if self.request.method == 'GET':
            return self._render_create_form()
        elif self.request.method == 'POST':
            return self._process_create_form()

    def _render_create_form(self, **kwargs):
        template_name = '/'.join([self.TEMPLATE_DIRECTORY_NAME, 'form.html'])
        return self.render_template(
            template_name,
            BASE_TEMPLATE_NAME='mvc/create.html',
            model_instance=None,
            **kwargs,
        )

    def _process_create_form(self):
        model_instance = self.MODEL_CLASS(**self.request.form)
        session = Database.create_session()
        session.add(model_instance)
        session.commit()
        session.close()
        return self._render_create_form(
            message='Model instance is created.',
        )
