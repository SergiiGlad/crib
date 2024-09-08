from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.auth import get_user_model


User = get_user_model()


class LogActivity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    old_data = models.JSONField()
    new_data = models.JSONField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def create(self,
               ct=None,
               instance=None,
               changes=None):
        self.objects.create(
            content_type=ContentType
        )