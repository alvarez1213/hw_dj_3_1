from django.db import models


class Phone(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, db_index=True, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.URLField()
    release_date = models.DateField()
    lte_exists = models.BooleanField()

    def __str__(self):
        return self.name
