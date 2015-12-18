from django.db import models


class Product(models.Model):

    name = models.CharField(max_length=500)
    priority = models.BooleanField(default=False)

    class Meta:
        db_table = 'product'
