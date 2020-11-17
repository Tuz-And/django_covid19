from django.db import models


class Covid19(models.Model):
    country = models.CharField(max_length=128)
    countrycode = models.CharField(max_length=10)
    slug = models.CharField(max_length=128)
    newconfirmed  = models.IntegerField(max_length=15)
    totalconfirmed = models.IntegerField()
    totaldeaths = models.IntegerField()
    nevrecovered = models.IntegerField()
    totalrecovered = models.IntegerField()

    class Meta:
        verbose_name = 'covid19'
        verbose_name_plural = 'covid19s'
