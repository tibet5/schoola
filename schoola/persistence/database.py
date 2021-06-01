import sqlalchemy
import sqlalchemy.orm
import sqlalchemy.ext.declarative


class Database(object):

    __ENGINE__ = sqlalchemy.create_engine('sqlite+pysqlite:///schoola.db')

    __SESSION_CLASS__ = sqlalchemy.orm.sessionmaker(__ENGINE__)

    __DECLARATIVE_BASE__ = sqlalchemy.ext.declarative.declarative_base()

    @classmethod
    def migrate(cls):
        import schoola.modules.instructors.models
        import schoola.modules.students.models
        import schoola.modules.advisors.models
        import schoola.modules.classrooms.models
        import schoola.modules.courses.models
        import schoola.modules.departments.models
        import schoola.modules.sections.models
        import schoola.modules.teaches.models
        import schoola.modules.prerequirements.models
        import schoola.modules.takes.models
        import schoola.modules.time_slots.models

        return cls.__DECLARATIVE_BASE__.metadata.create_all(
            cls.__ENGINE__,
        )

    @classmethod
    def create_session(cls):
        session = cls.__SESSION_CLASS__()
        return session
