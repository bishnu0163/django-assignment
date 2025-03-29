from django.db.models.signals import post_save   ## BY DEFAULT DJANGO SIGNALS ARE EXECUTED SYNCHRONOUSLY
from django.dispatch import receiver
from django.db import models
import time

class TestModel(models.Model):
    name = models.CharField(max_length=100)

@receiver(post_save, sender=TestModel)
def test_signal(sender, instance, **kwargs):
    print("Signal started")
    time.sleep(2) 
    print("Signal finished")

print("Before save")
TestModel.objects.create(name="test")
print("After save")                               