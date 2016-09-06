from django.db.models.signals import pre_save, pre_delete, post_save, post_delete
from django.dispatch import receiver
from django.conf import settings
import multidbexample.models as multidbexamplemodels
import os.path
from multidbexample.manager import MultiDBExampleManager

class MultiDBExampleSignal(object):
    @receiver(pre_save, sender=multidbexamplemodels.Publisher)
    @receiver(pre_save, sender=multidbexamplemodels.Author)
    def model_pre_save(sender, instance, **kwargs):
        print "*************** AUTHOR/PUBLISHER SIGNAL PRE SAVE ***********************"

    @receiver(post_save, sender=multidbexamplemodels.Publisher)
    @receiver(post_save, sender=multidbexamplemodels.Author)
    def model_post_save(sender, instance, **kwargs):
        print "*************** AUTHOR/PUBLISHER POST SAVE ***********************"
        if isinstance(instance, multidbexamplemodels.Publisher):
            print "publisher instance"
            manager = MultiDBExampleManager(instance.name)
            manager.migrate()
        else:
            print "default instance"


    #@receiver(pre_delete, sender=multidbexamplemodels.Publisher)
    @receiver(pre_delete, sender=multidbexamplemodels.Author)
    def model_pre_delete(sender, instance, **kwargs):
        print "*************** AUTHOR/PUBLISHER PRE DELETE ***********************"

    #@receiver(post_delete, sender=multidbexamplemodels.Publisher)
    @receiver(post_delete, sender=multidbexamplemodels.Author)
    def model_post_delete(sender, instance, **kwargs):
        print "*************** AUTHOR/PUBLISHER SIGNAL POST DELETE ***********************"