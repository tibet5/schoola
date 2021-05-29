from schoola.persistence import Database
from schoola.arch.mvc.mixins.singular_resource_querier_mixin import SingularResourceQuerierMixin


class DeleteMixin(SingularResourceQuerierMixin):

    TEMPLATE_DIRECTORY_NAME = None

    def handle_delete_request(self, id, *args, **kwargs):
        model_instance = self.get_model_instance_by_id(id)
        if self.request.method == 'GET':
            return self._render_delete_form(model_instance, **kwargs)
        elif self.request.method == 'POST':
            return self._process_delete_form(model_instance, **kwargs)

    def _render_delete_form(self, model_instance, **kwargs):
        template_name = 'mvc/delete.html'
        return self.render_template(
            template_name,
            model_instance=model_instance,
            **kwargs,
        )

    def _process_delete_form(self, model_instance, **kwargs):
        session = Database.create_session()
        session.delete(model_instance)
        session.commit()
        session.close()
        model_instance = None
        return self._render_delete_form(
            model_instance,
            message='Model instance is deleted.',
        )
