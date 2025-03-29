from django.db.models.signals import post_save   ##Django signals run in the same database transaction by default
from django.dispatch import receiver
from django.db import models, transaction

class TestModel(models.Model):
    name = models.CharField(max_length=100)

@receiver(post_save, sender=TestModel)
def test_signal(sender, instance, **kwargs):
    # This will be rolled back if transaction fails
    instance.name = "modified"
    instance.save()
    raise Exception("Force rollback")

try:
    with transaction.atomic():
        instance = TestModel.objects.create(name="original")
        print(f"Before commit: {TestModel.objects.get().name}")
except:
    print(f"After rollback: {TestModel.objects.get().name}")