import json

from django.db import models
from django.utils import timezone

from users.tasks.logs import create_log
from users.middleware.current_user import get_user, get_request
from django.contrib.contenttypes.models import ContentType


class BaseDbManager(models.Manager):
    def get_queryset(self):
        qs = super().get_queryset()

        # if `use_db` is set on model use that for choosing the DB
        if hasattr(self.model, 'use_db'):
            qs = qs.using(self.model.use_db)

        return qs


class BaseModel(models.Model):
    use_db = 'default'
    objects = BaseDbManager()

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def __str__(self):
        return f'{self.pk}.{self.name}' if getattr(self, 'name', None) else f'{self.pk}'

    def save(self, *args, **kwargs):
        if self.pk:  # Если объект уже существует в базе данных (не новая запись)
            old_instance = self.__class__.objects.get(pk=self.pk)
            changes = self.get_changes(old_instance)

            # Если есть изменения, логируем их
            if changes:
                create_log(
                    user=get_user(),
                    action="update",
                    ct=ContentType.objects.get_for_model(self).pk,
                    instance=self.pk,
                    changes=json.dumps(changes),
                    timestamp=timezone.now()
                )

        super(BaseModel, self).save(*args, **kwargs)

    def get_changes(self, old_instance):
        changes = {}
        for field in self._meta.fields:
            field_name = field.name
            old_value = getattr(old_instance, field_name)
            new_value = getattr(self, field_name)
            if old_value != new_value:
                changes[field_name] = {
                    "old": old_value,
                    "new": new_value
                }
        return changes