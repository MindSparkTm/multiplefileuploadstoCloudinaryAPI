# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.db import models
from cloudinary.models import CloudinaryField
from django.utils import timezone



from cloudinary.models import CloudinaryField

class Photo(models.Model):
  postid = models.AutoField(primary_key=True)
  created = models.DateTimeField(auto_now_add=True, editable=False)
  title = models.CharField(max_length=10000, null=True, blank=True)
  description = models.CharField(max_length=10000, null=True, blank=True)
  publicid = models.CharField(max_length=10000, null=True, blank=True)
  url = models.CharField(max_length=10000, null=True, blank=True)
