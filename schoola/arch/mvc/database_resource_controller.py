from schoola.arch.mvc.controller import Controller
import schoola.arch.mvc.mixins as mvc_mixins


class DatabaseResourceController(
    Controller,
    mvc_mixins.CreateMixin,
    mvc_mixins.ReadMixin,
    mvc_mixins.UpdateMixin,
    mvc_mixins.DeleteMixin,
    mvc_mixins.ListMixin,
):
    def get_model_instance_url(self):
        from schoola.inet.router import ROUTES_BY_NAME
        base_route_name_split = self.route_name.split('.')[:-1]
        creation_route_name = '.'.join([*base_route_name_split, 'create'])
        route = ROUTES_BY_NAME.get(creation_route_name)
        if not route:
            return None
        return route.get('path')

    def handle_request(self, *args, **kwargs):
        if self.route_name.endswith('.create'):
            return self.handle_create_request(*args, **kwargs)
        if self.route_name.endswith('.read'):
            return self.handle_read_request(*args, **kwargs)
        if self.route_name.endswith('.update'):
            return self.handle_update_request(*args, **kwargs)
        if self.route_name.endswith('.delete'):
            return self.handle_delete_request(*args, **kwargs)
        if self.route_name.endswith('.list'):
            return self.handle_list_request(*args, **kwargs)
        return self.route_name
