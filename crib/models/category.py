from django.db import models

from base.model import BaseModel


# Create your models here.
class Category(BaseModel):
    name = models.CharField(max_length=50)
    parent = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        pass
        # db_table = 'category'

    def __str__(self):
        return self.name
