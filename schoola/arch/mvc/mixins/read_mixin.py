from schoola.arch.mvc.mixins.singular_resource_querier_mixin import SingularResourceQuerierMixin


class ReadMixin(SingularResourceQuerierMixin):

    TEMPLATE_DIRECTORY_NAME = None

    MODEL_CLASS = None

    PRIMARY_KEYS = [
        'id'
    ]

    def handle_read_request(self, id, *args, **kwargs):
        model_instance = self.get_model_instance_by_id(id)
        template_name = 'mvc/read.html'
        thead_template_name = '/'.join([self.TEMPLATE_DIRECTORY_NAME, 'thead.html'])
        td_template_name = '/'.join([self.TEMPLATE_DIRECTORY_NAME, 'td.html'])
        return self.render_template(
            template_name,
            model_instance=model_instance,
            THEAD_TEMPLATE_NAME=thead_template_name,
            TD_TEMPLATE_NAME=td_template_name,
        )
