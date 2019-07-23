from django.db import models


class TinyUrl(models.Model):
    my_url = models.AutoField(primary_key=True)
    url = models.CharField(max_length=1000)

    class Meta:
        db_table = "tiny_url"

    def __str__(self):
        return f'{self.my_url} | {self.url}'

