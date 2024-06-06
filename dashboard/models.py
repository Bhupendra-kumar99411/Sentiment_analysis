from django.db import models

class BlackOffer(models.Model):
    end_year = models.IntegerField(null=True, default=None)
    intensity = models.IntegerField(null=True, default=None)
    sector = models.CharField(max_length=20, null=True, default=None)
    topic = models.CharField(max_length=20, null=True, default=None)
    insight = models.CharField(max_length=250, null=True, default=None)
    url = models.CharField(max_length=250, null=True, default=None)
    region = models.CharField(max_length=50, null=True, default=None)
    start_year = models.IntegerField(null=True, default=None)
    impact = models.IntegerField(null=True, default=None)
    added = models.DateTimeField(null=True, default=None)
    published = models.DateTimeField(null=True, default=None)
    country = models.CharField(max_length=100, null=True, default=None)
    relevance = models.IntegerField(null=True, default=None)
    pestle = models.CharField(max_length=50, null=True, default=None)
    source = models.CharField(max_length=50, null=True, default=None)
    title = models.CharField(max_length=250, null=True, default=None)
    likelihood = models.IntegerField(null=True, default=None)

class tweets(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField(null=True)
    hastag = models.CharField(null=True, max_length=50)
    username = models.CharField(null=True, max_length=50)
    tweets = models.TextField(null=True)
    sentiment = models.CharField(max_length=30, null=True)
