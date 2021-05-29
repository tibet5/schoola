
class MVCRoutingHelper(object):

    @classmethod
    def build_crudl_routes(cls, **kwargs):
        base_name = kwargs.get('base_name')
        base_path = kwargs.get('base_path')
        controller_class = kwargs.get('controller_class')
        exclude = kwargs.get('exclude', [])
        routes = []
        actions = {
            'create': {
                'path': 'create',
                'methods': [
                    'GET',
                    'POST',
                ],
            },
            'read': {
                'path': '<id>',
                'methods': [
                    'GET',
                ],
            },
            'update': {
                'path': '<id>/update',
                'methods': [
                    'GET',
                    'POST'
                ],
            },
            'delete': {
                'path': '<id>/delete',
                'methods': [
                    'GET',
                    'POST'
                ],
            },
            'list': {
                'path': '',
                'methods': [
                    'GET',
                ],
            },
        }
        for action, action_kwargs in actions.items():
            if action in exclude:
                continue
            route = {
                'name': '.'.join([base_name, action]),
                'path': '/'.join([base_path, action_kwargs.get('path')]),
                'methods': action_kwargs.get('methods'),
                'controller_class': controller_class,
            }
            routes.append(route)
        return routes
