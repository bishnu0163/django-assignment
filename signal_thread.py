from django.db.models.signals import post_save  ##Django signals run in the same thread as the caller by default
from django.dispatch import receiver
from django.db import models
import threading

class TestModel(models.Model):
    name = models.CharField(max_length=100)

@receiver(post_save, sender=TestModel)
def test_signal(sender, instance, **kwargs):
    print(f"Signal thread: {threading.current_thread().name}")

print(f"Main thread: {threading.current_thread().name}")
TestModel.objects.create(name="test")