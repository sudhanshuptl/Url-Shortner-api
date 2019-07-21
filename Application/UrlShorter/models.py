from django.db import models


class TinyUrl(models.Model):
    url_id = models.AutoField(primary_key=True)
    url = models.CharField(max_length=200)

    class Meta:
        db_table = "tiny_url"

