
import multidbexample.models as multidbexamplemodels
from DjangoExamples import settings

class MultiDBExampleRouter(object):

    def db_for_read(self, model, **hints):
        database = getattr(model, "_DATABASE", None)
        instance = hints.get('instance')

        print "db_for_read: " + model._meta.label

        print hints

        return database

        if isinstance(instance, multidbexamplemodels.Author):
            print settings.DATABASES.keys()
            print "db_for_read: " + model._meta.label + " using database " + instance.publisher.name
            return instance.publisher.name
        else:
            print "db_for_read: " + model._meta.label + " using default database"

        return "default"

    def db_for_write(self, model, **hints):
        database = getattr(model, "_DATABASE", None)
        instance = hints.get('instance')

        print "db_for_write: " + model._meta.label

        print hints

        return database

        if isinstance(instance, multidbexamplemodels.Author):
            print settings.DATABASES.keys()
            print "db_for_write: " + model._meta.label + " using database " + instance.publisher.name
            return instance.publisher.name
        else:
            print "db_for_write: " + model._meta.label + " using default database"

        return "default"

    def allow_relation(self, obj1, obj2, **hints):
        return obj1._state.db == obj2._state.db

    def allow_syncdb(self, db, model):
        return True
