import os
import sys
from django.core.management import execute_from_command_line
from DjangoExamples import settings

class MultiDBExampleManager(object):
    def __init__(self, new_db_name):
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DjangoExamples.settings")
        self.db_name = new_db_name
        self.db_file = os.path.join(settings.BASE_DIR, self.db_name + '.sqlite3')

        if new_db_name in settings.DATABASES.keys() and os.path.exists(self.db_file):
            self.db = settings.DATABASES[new_db_name]
            self.db_file = self.db['NAME']
        else:
            self.db  = settings.DATABASES['default']
            self.db['NAME'] = self.db_file
            settings.DATABASES[self.db_name] = self.db

        print settings.DATABASES

    def make_migrations(self):
        execute_from_command_line(['manage.py', 'makemigrations'])

    def migrate(self):
        arg = '--database=' + self.db_name
        execute_from_command_line(['manage.py', 'migrate', arg])

    def db_clean(self):
        os.remove(self.db_file) if os.path.exists(self.db_file) else None