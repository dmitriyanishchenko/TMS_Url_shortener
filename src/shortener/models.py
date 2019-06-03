from django.db import models


class ShortUrl(models.Model):
    original_url = models.CharField(max_length=150)
    short_url = models.CharField(max_length=150)
    add = models.DateTimeField(null=False)
    counter_click = models.PositiveSmallIntegerField()

    def __str__(self):
        return f' {self.original_url} - {self.short_url}'





# Create your models here.
