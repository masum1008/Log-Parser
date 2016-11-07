import json
import copy
import functools

import sqlalchemy as sa
from sqlalchemy import orm, types, Column, Table
from django.conf import settings

DB_ENGINE = settings.DATABASES['default']['ENGINE'].rpartition('.')[-1]

# def init_defaults(cls, **defaults):
#    def wrap_init(fn):
#        extra_defaults = defaults
#        @functools.wraps(fn)
#        def wrapper(self, *args, **kwargs):
#            for k, v in extra_defaults.iteritems():
#                kwargs.setdefault(k, v)
#            fn(self, *args, **kwargs)
#
#        return wrapper
#
#    cls.__init__ = wrap_init(cls.__init__)
#
#
# init_defaults(Table, quote=True)
# init_defaults(Column, quote=True, quote_schema=True)

if DB_ENGINE == 'postgresql_psycopg2':
    connection_string = ('postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{NAME}').format(**settings.DATABASES['default'])
else:
    connection_string = ('{0}://{USER}:{PASSWORD}@{HOST}:{PORT}/{NAME}').format(DB_ENGINE,
                                                                                **settings.DATABASES['default'])

if DB_ENGINE == 'mysql':
    connection_string += '?charset=utf8'

metaData = sa.MetaData()

engine = sa.create_engine(connection_string, pool_recycle=3600, pool_size=20, max_overflow=-1)
metaData.bind = engine
engine.echo = False


def versioned_objects(sequence):
    return (obj for obj in sequence if getattr(obj, '__history__', False))


class VersionedListener(orm.interfaces.SessionExtension):
    def before_flush(self, session, flush_context, instances):
        from divineba.system.models import create_version

        for obj in versioned_objects(session.new):
            obj.version = 1
        for obj in versioned_objects(session.dirty):
            create_version(obj, session)
        for obj in versioned_objects(session.deleted):
            create_version(obj, session, deleted=True)


session_maker = sa.orm.sessionmaker(bind=engine, autoflush=False, extension=VersionedListener())


def create_session():
    return sa.orm.scoped_session(session_maker)


class JSONField(types.MutableType, types.TypeDecorator):
    impl = types.Text

    def process_bind_param(self, value, dialect):
        return json.dumps(value)

    def process_result_value(self, value, dialect):
        # Double conversion ensures proper deserialization of list, dict etc
        try:
            value = json.loads(value)
            return json.loads(value)
        except (TypeError, ValueError):
            return value

    def copy_value(self, value):
        return copy.copy(value)


class JSONSet(types.MutableType, types.TypeDecorator):
    impl = types.Text

    def process_bind_param(self, value, dialect):
        return json.dumps(list(value))

    def process_result_value(self, value, dialiect):
        return set(json.loads(value))

    def copy_value(self, value):
        return set(json.loads(json.dumps(list(value))))



