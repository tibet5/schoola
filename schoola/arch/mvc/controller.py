
class Controller(object):

    BASE_TITLE = 'Schoola'

    TITLE = None

    PAGE_HEADER = None

    def __init__(self, *args, **kwargs):
        self.route_name = kwargs.get('route_name')
        self.request = kwargs.get('request')
        self._render_template = kwargs.get('render_template')

    def _get_title(self):
        segments = []
        if self.TITLE:
            segments.append(self.TITLE)
        if self.BASE_TITLE:
            segments.append(self.BASE_TITLE)
        return ' | '.join(segments)

    def _get_page_header(self):
        if (self.PAGE_HEADER):
            return self.PAGE_HEADER
        if (self.PAGE_HEADER and self.PAGE_HEADER != 'INDEX'):
            route_name_split = self.route_name.split('.')
            segments = []
            segments.append(route_name_split[-1])
            segments.append(route_name_split[-2])
            header = ' '.join(segments)
            header = header.title()
            return header

    def render_template(self, template_name, **kwargs):
        if 'TITLE' not in kwargs:
            kwargs['TITLE'] = self._get_title()
        if 'PAGE_HEADER' not in kwargs:
            kwargs['PAGE_HEADER'] = self._get_page_header()
        if 'CREATE_MODEL_INSTANCE_URL' not in kwargs and hasattr(self, 'get_model_instance_url'):
            kwargs['CREATE_MODEL_INSTANCE_URL'] = self.get_model_instance_url()
        return self._render_template(
            template_name,
            **kwargs,
        )

    #def handle_request(self, *args, **kwargs):
    #    pass
