from django.db import models


class City(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, blank=True)

    class Meta:
        verbose_name = "City"
        verbose_name_plural = "Cities"

    def __str__(self):
        return self.name

