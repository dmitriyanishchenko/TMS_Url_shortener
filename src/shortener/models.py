from django.db import models


class ShortUrls(models.Model):
    long_url = models.URLField()
    short_url = models.CharField(max_length=20)
    date_add = models.DateTimeField(auto_now_add=True)
    counter = models.IntegerField(default=0)

    class Meta:
        ordering = ['-counter']

    def __str__(self):
        return f' {self.long_url}'
