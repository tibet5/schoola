from schoola.persistence import Database
from schoola.arch.mvc.mixins.singular_resource_querier_mixin import SingularResourceQuerierMixin


class UpdateMixin(SingularResourceQuerierMixin):

    TEMPLATE_DIRECTORY_NAME = None

    def handle_update_request(self, id, *args, **kwargs):
        model_instance = self.get_model_instance_by_id(id)
        if self.request.method == 'GET':
            return self._render_update_form(
                model_instance=model_instance,
            )
        elif self.request.method == 'POST':
            return self._process_update_form(
                model_instance=model_instance,
            )

    def _render_update_form(self, **kwargs):
        template_name = '/'.join([self.TEMPLATE_DIRECTORY_NAME, 'form.html'])
        return self.render_template(
            template_name,
            BASE_TEMPLATE_NAME='mvc/update.html',
            **kwargs,
        )

    def _process_update_form(self, *args, **kwargs):
        session = Database.create_session()
        model_instance = kwargs.get('model_instance')
        for key, value in self.request.form.items():
            if hasattr(model_instance, key):
                setattr(model_instance, key, value)
        model_instance = session.merge(model_instance)
        session.commit()
        return self._render_update_form(
            model_instance=model_instance,
            message='Model instance is updated.'
        )
