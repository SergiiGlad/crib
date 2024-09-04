from django.db import models


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
