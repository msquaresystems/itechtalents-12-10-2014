from django.db import models
from django.contrib.auth.models import User


class VideoResume(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=200, blank=True)
    guid = models.CharField(max_length=50, blank=True)
    is_default = models.BooleanField(default=False)
    is_removed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
    	return "Video: %s" % self.guid