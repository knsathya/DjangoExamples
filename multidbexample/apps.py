from __future__ import unicode_literals

from django.apps import AppConfig


class MultidbexampleConfig(AppConfig):
    name = 'multidbexample'

    def ready(self):
        import multidbexample.signals