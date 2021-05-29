from schoola.persistence import Database


class ListMixin(object):

    TEMPLATE_DIRECTORY_NAME = None

    MODEL_CLASS = None

    def handle_list_request(self, *args, **kwargs):
        session = Database.create_session()
        model_instances = session.query(
            self.MODEL_CLASS,
        ).all()
        session.close()
        template_name = 'mvc/list.html'
        thead_template_name = '/'.join([self.TEMPLATE_DIRECTORY_NAME, 'thead.html'])
        td_template_name = '/'.join([self.TEMPLATE_DIRECTORY_NAME, 'td.html'])
        return self.render_template(
            template_name,
            model_instances=model_instances,
            THEAD_TEMPLATE_NAME=thead_template_name,
            TD_TEMPLATE_NAME=td_template_name,
        )
