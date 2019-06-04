from django.db import models


class ShortUrl(models.Model):
    full_url = models.CharField(max_length=150)
    short_url = models.CharField(max_length=150)
    date_add = models.DateTimeField(null=False)
    counter_click = models.IntegerField()

    def __str__(self):
        return f' {self.full_url} - {self.short_url}'





# Create your models here.
