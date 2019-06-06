from django.db import models


class Short_urls(models.Model):
    long_url = models.URLField("URL", unique=True)
    short_url = models.CharField(max_length=20)
    date_add = models.DateTimeField(auto_now_add=True)
    counter = models.IntegerField(default=0)

    def __str__(self):
        return f' {self.long_url} - {self.counter}'





# Create your models here.
