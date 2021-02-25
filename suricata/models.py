from django.db import models


class SuriMonitor(models.Model):
    project = models.CharField(max_length=63)
    sid = models.IntegerField(blank=True, null=True)
    times = models.IntegerField(blank=True, null=True)
    cnts = models.IntegerField(blank=True, null=True)
    threatname = models.CharField(max_length=255, blank=True, null=True)
    tips = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'suri_monitor'
