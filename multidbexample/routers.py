
import multidbexample.models as multidbexamplemodels

class MultiDBExampleRouter(object):

    def db_for_read(self, model, **hints):
        database = getattr(model, "_DATABASE", None)
        instance = hints.get('instance')

        print hints

        if instance:
            print "db_for_read: " + type(instance).__name__

        if isinstance(instance, multidbexamplemodels.Author):
            return instance.publisher.name
        else:
            print "default instance"

        return "default"

    def db_for_write(self, model, **hints):
        database = getattr(model, "_DATABASE", None)
        instance = hints.get('instance')

        if instance:
            print "db_for_write: " + type(instance).__name__

        if isinstance(instance, multidbexamplemodels.Author):
            return instance.publisher.name
        else:
            print "default instance"

        return "default"

    def allow_relation(self, obj1, obj2, **hints):
        return obj1._state.db == obj2._state.db

    def allow_syncdb(self, db, model):
        return True
