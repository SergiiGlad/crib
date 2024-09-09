from django.db import models
from django.contrib.auth import get_user_model
from base.model import BaseModel


User = get_user_model()


# Create your models here.
class Category(BaseModel):
    name = models.CharField(max_length=50)
    parent = models.ManyToManyField("self", null=True, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        pass
        # db_table = 'category'

