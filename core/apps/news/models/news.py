from django.db import models

from core.apps.common.models import TimedBaseModel


class News(TimedBaseModel):
    title = models.CharField(verbose_name="Новость", max_length=255)
    content = models.TextField(verbose_name="Содержание", blank=True, default="")
    is_active = models.BooleanField(verbose_name="Активна", default=True)

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"

    def __str__(self):
        return self.title
