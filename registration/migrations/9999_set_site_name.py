# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def set_site_name(apps, schema_editor):
    from django.conf import settings
    from django.contrib.sites.models import Site
    site = Site.objects.get(id=settings.SITE_ID)
    site.domain = settings.SITE_NAME
    site.name = settings.SITE_NAME
    site.save()


class Migration(migrations.Migration):

    dependencies = [('sites', '__first__')]

    operations = [
        migrations.RunPython(set_site_name),
    ]
