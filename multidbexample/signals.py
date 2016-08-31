from django.db.models.signals import pre_save, pre_delete, post_save, post_delete
from django.dispatch import receiver
from django.conf import settings
import multidbexample.models as multidbexamplemodels
import os.path