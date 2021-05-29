from schoola.persistence import Database


class SingularResourceQuerierMixin(object):

    MODEL_CLASS = None

    PRIMARY_KEYS = [
        'id',
    ]

    def get_model_instance_by_id(self, id):
        session = Database.create_session()
        filters = []
        ids_split = id.split('-')
        for pk_idx, pk_name in enumerate(self.PRIMARY_KEYS):
            filters.append(getattr(self.MODEL_CLASS, pk_name) == ids_split[pk_idx])
        model_instance = session.query(
            self.MODEL_CLASS,
        ).filter(
            *filters,
        ).first()
        session.close()
        return model_instance
