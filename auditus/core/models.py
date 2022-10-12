from django.db import models

from uuid import uuid4


class AbstractBaseModel(models.Model):
    uuid = models.UUIDField(
        verbose_name=('uuid'), default=uuid4, editable=False, unique=True
    )
    created_at = models.DateTimeField(verbose_name=('created at'), auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name=('updated at'), auto_now=True)

    class Meta:
        abstract = True

    def __str__(self):
        return str(self.pk)
