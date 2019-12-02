import uuid
from django.db import models
from django.db.models import Subquery, OuterRef



class Device(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    device_name = models.CharField(max_length=200, null=True, blank=True )
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.device_name)

class StatusActivity(models.Model):
    OFFLINE = 1
    ONLINE = 2
    STATUS = (
        (OFFLINE, ('Offline')),
        (ONLINE, ('Online')),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    device = models.ForeignKey(Device, related_name='status_activity', on_delete=models.CASCADE)
    status = models.PositiveSmallIntegerField(choices=STATUS)
    modified_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        get_latest_by = ['modified_at']


    def __str__(self):
        return str(self.device)
